# Bandit

[https://overthewire.org/wargames/bandit/](https://overthewire.org/wargames/bandit/)

## Level 0

### Task

The goal of this level is for you to log into the game using SSH. The host to which you need to connect is `bandit.labs.overthewire.org`, on port `2220`. The username is `bandit0` and the password is `bandit0`. Once logged in, go to the Level 1 page to find out how to beat Level 1.

### Solution

Simply use the command `ssh`:

```
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

and insert the password `bandit0` when asked for it.

## Level 1

### Task

The password for the next level is stored in a file called `readme` located in the home directory. Use this password to log into `bandit1` using SSH. Whenever you find a password for a level, use SSH (on port `2220`) to log into that level and continue the game.

### Solution

```
bandit0@bandit:~$ ls
readme
bandit0@bandit:~$ cat readme
NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL
```

## Level 2

### Task

The password for the next level is stored in a file called `-` located in the home directory

### Solution

```
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ cat ./-
rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi
```

## Level 3

### Task

The password for the next level is stored in a file called `spaces in this filename` located in the home directory.

### Solution

```
bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ cat "spaces in this filename"
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
```

## Level 4

### Task

The password for the next level is stored in a hidden file in the `inhere` directory.

### Solution

```
bandit3@bandit:~$ ls
inhere
bandit3@bandit:~$ ls inhere/
bandit3@bandit:~$ ls -a inhere/
.  ..  .hidden
bandit3@bandit:~$ cat inhere/.hidden
2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe
```

## Level 5

### Task

The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the `reset` command.

### Solution

```
bandit4@bandit:~$ ls
inhere
bandit4@bandit:~$ ls inhere/
-file00  -file02  -file04  -file06  -file08
-file01  -file03  -file05  -file07  -file09
bandit4@bandit:~$ for file in $(ls inhere/); do file inhere/$file; done
inhere/-file00: data
inhere/-file01: data
inhere/-file02: data
inhere/-file03: data
inhere/-file04: data
inhere/-file05: data
inhere/-file06: data
inhere/-file07: ASCII text
inhere/-file08: data
inhere/-file09: data
bandit4@bandit:~$ cat inhere/-file07
lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR
```

## Level 6

### Task

The password for the next level is stored in a file somewhere under the `inhere` directory and has all of the following properties:

- human-readable,
- 1033 bytes in size,
- not executable.

### Solution

```
bandit5@bandit:~$ ls
inhere
bandit5@bandit:~$ find inhere/ -size 1033c
inhere/maybehere07/.file2
bandit5@bandit:~$ cat inhere/maybehere07/.file2
P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU
```

## Level 7

### Task

The password for the next level is stored somewhere on the server and has all of the following properties:

- owned by user `bandit7`,
- owned by group `bandit6`,
- 33 bytes in size.

### Solution

```
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S
```

## Level 8

### Task

The password for the next level is stored in the file `data.txt` next to the word "millionth".

### Solution

```
bandit7@bandit:~$ ls
data.txt
bandit7@bandit:~$ grep -A 3 -B 3 millionth data.txt
sermon's	F5B9EHIT1tI56VfczeBtEHWGlSTS0SWl
hoe's	HhTKj3PgrBCYxn8BAHgWg3aYyQPwNs4b
huffy	WJDdimZChuTlmWvX1f00KQgSd3DI63in
millionth	TESKZC0XvTetK0S9xNwm25STk5iWrBvP
Roderick's	zbqXMhsLoFPqc2Mf0TJwI7H6KXp75PSi
cleanup's	ptKYlwR6eOUNk2TM9jxcsg225y6CQZVa
lassie's	Bg8NBxvkuwpoyzw56P3TnFnSEqCFGpDl
bandit7@bandit:~$ grep millionth data.txt
millionth	TESKZC0XvTetK0S9xNwm25STk5iWrBvP
```

## Level 9

### Task

The password for the next level is stored in the file `data.txt` and is the only line of text that occurs only once.

### Solution

```
bandit8@bandit:~$ ls
data.txt
bandit8@bandit:~$ sort data.txt | uniq -u
EN632PlfYiZbn3PhVK3XOGSlNInNE00t
```

## Level 10

### Task

The password for the next level is stored in the file `data.txt` in one of the few human-readable strings, preceded by several `=` characters.

### Solution

```
bandit9@bandit:~$ cat data.txt | strings | grep =
=2""L(
x]T========== theG)"
========== passwordk^
Y=xW
t%=q
========== is
4=}D3
{1\=
FC&=z
=Y!m
	$/2`)=Y
4_Q=\
MO=(
?=|J
WX=DA
{TbJ;=l
[=lI
========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
>8=6
=r=_
=uea
zl=4
```

## Level 11

### Task

The password for the next level is stored in the file `data.txt`, which contains base64 encoded data.

### Solution

```
bandit10@bandit:~$ ls
data.txt
bandit10@bandit:~$ cat data.txt
VGhlIHBhc3N3b3JkIGlzIDZ6UGV6aUxkUjJSS05kTllGTmI2blZDS3pwaGxYSEJNCg==
bandit10@bandit:~$ cat data.txt | base64 -d
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
```

## Level 12

### Task

The password for the next level is stored in the file `data.txt`, where all lowercase (`a-z`) and uppercase (`A-Z`) letters have been rotated by 13 positions.

### Solution

```
bandit11@bandit:~$ ls
data.txt
bandit11@bandit:~$ cat data.txt
Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi
```

[Here](https://stackoverflow.com/questions/5442436/using-rot13-and-tr-command-for-having-an-encrypted-email-address) one finds something about Rot13:

```
echo 'fooman@example.com' | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

and

```
alias rot13="tr 'A-Za-z' 'N-ZA-Mn-za-m'"
```

Thus:

```
bandit11@bandit:~$ alias rot13="tr 'A-Za-z' 'N-ZA-Mn-za-m'"
bandit11@bandit:~$ cat data.txt | rot13
The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv
```

## Leve 13

### Task

The password for the next level is stored in the file `data.txt`, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under `/tmp` in which you can work. Use `mkdir` with a hard to guess directory name. Or better, use the command `mktemp -d`. Then copy the datafile using `cp`, and rename it using `mv` (read the manpages!).

### Solution

```
bandit12@bandit:~$ ls
data.txt
bandit12@bandit:~$ mkdir /tmp/mysecrettmpdir
bandit12@bandit:~$ cd /tmp/mysecrettmpdir
bandit12@bandit:/tmp/mysecrettmpdir$ xxd -r data.txt > a
bandit12@bandit:/tmp/mysecrettmpdir$ ls -l
total 8
-rw-rw-r-- 1 bandit12 bandit12  606 Apr 25 19:58 a
-rw-r----- 1 bandit12 bandit12 2582 Apr 25 19:57 data.txt
bandit12@bandit:/tmp/mysecrettmpdir$ file a
a: gzip compressed data, was "data2.bin", last modified: Thu Oct  5 06:19:20 2023, max compression, from Unix, original size modulo 2^32 573
bandit12@bandit:/tmp/mysecrettmpdir$ mv a a.gz
bandit12@bandit:/tmp/mysecrettmpdir$ gunzip a.gz
bandit12@bandit:/tmp/mysecrettmpdir$ ls
a  data.txt
bandit12@bandit:/tmp/mysecrettmpdir$ file a
a: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/mysecrettmpdir$ mv a a.bz2
bandit12@bandit:/tmp/mysecrettmpdir$ bzip2 -d a.bz2
bandit12@bandit:/tmp/mysecrettmpdir$ ls -l
total 8
-rw-rw-r-- 1 bandit12 bandit12  431 Apr 25 19:58 a
-rw-r----- 1 bandit12 bandit12 2582 Apr 25 19:57 data.txt
bandit12@bandit:/tmp/mysecrettmpdir$ file a
a: gzip compressed data, was "data4.bin", last modified: Thu Oct  5 06:19:20 2023, max compression, from Unix, original size modulo 2^32 20480
bandit12@bandit:/tmp/mysecrettmpdir$ mv a a.gz
bandit12@bandit:/tmp/mysecrettmpdir$ gunzip a
bandit12@bandit:/tmp/mysecrettmpdir$ ls
a  data.txt
bandit12@bandit:/tmp/mysecrettmpdir$ file a
a: POSIX tar archive (GNU)
bandit12@bandit:/tmp/mysecrettmpdir$ mv a a.tar
bandit12@bandit:/tmp/mysecrettmpdir$ tar -xvf a.tar
data5.bin
bandit12@bandit:/tmp/mysecrettmpdir$ file data5.bin
data5.bin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/mysecrettmpdir$ mv data5.bin b.tar
bandit12@bandit:/tmp/mysecrettmpdir$ tar tvf b.tar
-rw-r--r-- root/root       217 2023-10-05 06:19 data6.bin
bandit12@bandit:/tmp/mysecrettmpdir$ tar xvf b.tar
data6.bin
bandit12@bandit:/tmp/mysecrettmpdir$ file data6.bin
data6.bin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/mysecrettmpdir$ mv data6.bin c.bz2
bandit12@bandit:/tmp/mysecrettmpdir$ bzip2 -d c.bz2
bandit12@bandit:/tmp/mysecrettmpdir$ ls
a.tar  b.tar  c  data.txt
bandit12@bandit:/tmp/mysecrettmpdir$ file c
c: POSIX tar archive (GNU)
bandit12@bandit:/tmp/mysecrettmpdir$ mv c c.tar
bandit12@bandit:/tmp/mysecrettmpdir$ tar tvf c.tar
-rw-r--r-- root/root        79 2023-10-05 06:19 data8.bin
bandit12@bandit:/tmp/mysecrettmpdir$ tar xvf c.tar
data8.bin
bandit12@bandit:/tmp/mysecrettmpdir$ file data8.bin
data8.bin: gzip compressed data, was "data9.bin", last modified: Thu Oct  5 06:19:20 2023, max compression, from Unix, original size modulo 2^32 49
9:20 2023, max compression, from Unix, original size modulo 2^32 49
bandit12@bandit:/tmp/mysecrettmpdir$ mv data8.bin d.gz
bandit12@bandit:/tmp/mysecrettmpdir$ gunzip d.gz
bandit12@bandit:/tmp/mysecrettmpdir$ ls
a.tar  b.tar  c.tar  d  data.txt
bandit12@bandit:/tmp/mysecrettmpdir$ file d
d: ASCII text
bandit12@bandit:/tmp/mysecrettmpdir$ cat d
The password is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw
```
