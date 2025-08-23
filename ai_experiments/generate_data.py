import argparse
import logging
import os
import random
import time
from urllib.parse import urlparse, urljoin
from collections import defaultdict

import requests
from bs4 import BeautifulSoup
import tqdm
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('crawler.log'), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)


class WebCrawler:
    def __init__(self, seed_urls, max_pages=100, delay=1, lang='english'):
        self.seed_urls = seed_urls
        self.max_pages = max_pages
        self.delay = delay
        self.visited_urls = set()
        self.to_visit = set(seed_urls)
        self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
        self.lang = lang

        # Try to download NLTK resources if needed
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')

        try:
            nltk.data.find(f'corpora/stopwords')
        except LookupError:
            nltk.download('stopwords')

        self.stopwords = set(stopwords.words(lang))

    def get_page_content(self, url):
        """Fetch page content with proper headers and error handling"""
        try:
            headers = {
                'User-Agent': self.user_agent,
                'Accept': 'text/html,application/xhtml+xml,application/xml',
                'Accept-Language': 'en-US,en;q=0.9',
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            return None

    def extract_links(self, url, html):
        """Extract links from HTML content"""
        try:
            soup = BeautifulSoup(html, 'html.parser')
            base_url = urlparse(url).scheme + '://' + urlparse(url).netloc

            links = []
            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href']
                if href.startswith('#') or href.startswith('javascript:'):
                    continue

                # Make relative URLs absolute
                if not href.startswith(('http://', 'https://')):
                    href = urljoin(base_url, href)

                # Stay on the same domain
                if urlparse(href).netloc == urlparse(url).netloc:
                    links.append(href)

            return links
        except Exception as e:
            logger.error(f"Error extracting links from {url}: {e}")
            return []

    def extract_text(self, html):
        """Extract clean text from HTML"""
        try:
            soup = BeautifulSoup(html, 'html.parser')

            # Remove script and style elements
            for script in soup(["script", "style", "header", "footer", "nav"]):
                script.extract()

            # Get text
            text = soup.get_text(separator=' ')

            # Break into lines and remove leading/trailing whitespace
            lines = (line.strip() for line in text.splitlines())
            # Break multi-line text into paragraphs
            paragraphs = [line for line in lines if line]

            # Join paragraphs with newlines
            clean_text = '\n'.join(paragraphs)

            return clean_text
        except Exception as e:
            logger.error(f"Error extracting text: {e}")
            return ""

    def crawl(self):
        """Main crawling method"""
        collected_texts = []

        with tqdm.tqdm(total=self.max_pages, desc="Crawling websites") as pbar:
            while self.to_visit and len(self.visited_urls) < self.max_pages:
                # Get URL from queue
                url = self.to_visit.pop()

                # Skip if already visited
                if url in self.visited_urls:
                    continue

                # Mark as visited
                self.visited_urls.add(url)

                # Get page content
                html = self.get_page_content(url)
                if not html:
                    continue

                # Extract text
                text = self.extract_text(html)
                if text:
                    collected_texts.append(text)

                # Extract links and add to queue
                links = self.extract_links(url, html)
                for link in links:
                    if link not in self.visited_urls:
                        self.to_visit.add(link)

                pbar.update(1)
                time.sleep(self.delay)

        logger.info(
            f"Crawled {len(self.visited_urls)} pages, collected {len(collected_texts)} text samples")
        return collected_texts


def clean_sentence(sentence):
    """Clean and normalize a sentence"""
    # Remove leading/trailing whitespace
    sentence = sentence.strip()

    # Replace multiple spaces with a single space
    sentence = ' '.join(sentence.split())

    # Remove sentences that are too short or contain just numbers
    if len(sentence) < 20 or sentence.isdigit():
        return None

    return sentence


def generate_sentence_pairs(texts, min_length=5, max_length=30):
    """Generate sentence pairs from collected texts"""
    sentence_pairs = []

    for text in texts:
        # Split text into sentences
        sentences = sent_tokenize(text)

        # Skip if we don't have enough sentences
        if len(sentences) < 2:
            continue

        # Generate pairs of adjacent sentences
        for i in range(len(sentences) - 1):
            src = clean_sentence(sentences[i])
            tgt = clean_sentence(sentences[i + 1])

            # Skip if either sentence is None or too short/long
            if not src or not tgt:
                continue

            src_tokens = src.split()
            tgt_tokens = tgt.split()

            if min_length <= len(src_tokens) <= max_length and min_length <= len(tgt_tokens) <= max_length:
                sentence_pairs.append((src, tgt))

    # Shuffle to randomize
    random.shuffle(sentence_pairs)
    return sentence_pairs


def generate_reversal_pairs(texts, min_length=5, max_length=20):
    """Generate reversal pairs from sentences"""
    reversal_pairs = []

    for text in texts:
        # Split text into sentences
        sentences = sent_tokenize(text)

        for sentence in sentences:
            clean_sent = clean_sentence(sentence)
            if not clean_sent:
                continue

            tokens = clean_sent.split()
            if min_length <= len(tokens) <= max_length:
                src = ' '.join(tokens)
                tgt = ' '.join(reversed(tokens))
                reversal_pairs.append((src, tgt))

    # Shuffle to randomize
    random.shuffle(reversal_pairs)
    return reversal_pairs


def generate_vocab(sentence_pairs, min_freq=5):
    """Generate vocabulary from sentence pairs"""
    word_freq = defaultdict(int)

    for src, tgt in sentence_pairs:
        for word in src.split() + tgt.split():
            word_freq[word.lower()] += 1

    # Filter by minimum frequency
    vocab = [word for word, freq in word_freq.items() if freq >= min_freq]

    # Add special tokens
    special_tokens = ['<pad>', '<unk>', '<s>', '</s>']
    vocab = special_tokens + vocab

    logger.info(f"Generated vocabulary with {len(vocab)} words")
    return vocab


def save_data(sentence_pairs, output_file, split_ratio=0.1):
    """Save sentence pairs to file with train/val split"""
    # Split into train and validation sets
    split_idx = int(len(sentence_pairs) * (1 - split_ratio))
    train_pairs = sentence_pairs[:split_idx]
    val_pairs = sentence_pairs[split_idx:]

    # Save training data
    train_file = output_file
    with open(train_file, 'w', encoding='utf-8') as f:
        for src, tgt in train_pairs:
            f.write(f"{src}\t{tgt}\n")

    # Save validation data
    val_file = output_file.replace('.txt', '_val.txt')
    with open(val_file, 'w', encoding='utf-8') as f:
        for src, tgt in val_pairs:
            f.write(f"{src}\t{tgt}\n")

    logger.info(f"Saved {len(train_pairs)} training samples to {train_file}")
    logger.info(f"Saved {len(val_pairs)} validation samples to {val_file}")


def save_vocab(vocab, output_file):
    """Save vocabulary to file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        for word in vocab:
            f.write(f"{word}\n")

    logger.info(f"Saved vocabulary with {len(vocab)} words to {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Web Crawler Data Generator")
    parser.add_argument('--urls', nargs='+', required=True,
                        help='Seed URLs to start crawling')
    parser.add_argument('--max_pages', type=int, default=100,
                        help='Maximum number of pages to crawl')
    parser.add_argument('--delay', type=float, default=1.0,
                        help='Delay between requests in seconds')
    parser.add_argument('--output', type=str, default='data.txt',
                        help='Output file for generated data')
    parser.add_argument('--mode', type=str, choices=['sequence', 'reversal'], default='sequence',
                        help='Type of data to generate: sequence (next sentence) or reversal')
    parser.add_argument('--min_length', type=int, default=5,
                        help='Minimum sentence length in tokens')
    parser.add_argument('--max_length', type=int, default=20,
                        help='Maximum sentence length in tokens')
    parser.add_argument('--min_freq', type=int, default=5,
                        help='Minimum word frequency for vocabulary')

    args = parser.parse_args()

    # Create crawler
    crawler = WebCrawler(args.urls, args.max_pages, args.delay)

    # Crawl websites
    texts = crawler.crawl()

    if not texts:
        logger.error("No text collected. Exiting.")
        return

    # Generate sentence pairs based on mode
    if args.mode == 'sequence':
        sentence_pairs = generate_sentence_pairs(
            texts, args.min_length, args.max_length)
        logger.info(f"Generated {len(sentence_pairs)} sequence pairs")
    else:  # reversal
        sentence_pairs = generate_reversal_pairs(
            texts, args.min_length, args.max_length)
        logger.info(f"Generated {len(sentence_pairs)} reversal pairs")

    # Generate vocabulary
    vocab = generate_vocab(sentence_pairs, args.min_freq)

    # Save data and vocabulary
    save_data(sentence_pairs, args.output)
    save_vocab(vocab, 'vocab.txt')


if __name__ == "__main__":
    main()
