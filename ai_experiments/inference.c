// gcc inference.c -I/path/to/onnxruntime/include -L/path/to/onnxruntime/lib -lonnxruntime -o inference

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "onnxruntime_c_api.h"

#define MAX_SEQ_LEN 20
#define VOCAB_SIZE 13

// --- Simple Vocabulary & Tokenization Functions ---

typedef struct
{
    const char *token;
    int id;
} VocabEntry;

VocabEntry vocab[] = {
    {"<s>", 0},
    {"</s>", 1},
    {"<pad>", 2},
    {"hello", 3},
    {"world", 4},
    {"this", 5},
    {"is", 6},
    {"a", 7},
    {"test", 8},
    {"example", 9},
    {"of", 10},
    {"transformer", 11},
    {".", 12},
};

int tokenize(const char *input, int *output, int max_len)
{
    int count = 0;
    char *copy = strdup(input);
    char *token = strtok(copy, " \n\r");
    while (token && count < max_len)
    {
        int token_id = 2; // default to <pad> if not found
        for (size_t i = 0; i < sizeof(vocab) / sizeof(vocab[0]); i++)
        {
            if (strcmp(token, vocab[i].token) == 0)
            {
                token_id = vocab[i].id;
                break;
            }
        }
        output[count++] = token_id;
        token = strtok(NULL, " \n\r");
    }
    free(copy);
    return count;
}

void detokenize(const int *token_ids, int length, char *output, int out_size)
{
    output[0] = '\0';
    for (int i = 0; i < length; i++)
    {
        const char *token = "<unk>";
        for (size_t j = 0; j < sizeof(vocab) / sizeof(vocab[0]); j++)
        {
            if (vocab[j].id == token_ids[i])
            {
                token = vocab[j].token;
                break;
            }
        }
        strncat(output, token, out_size - strlen(output) - 1);
        if (i < length - 1)
        {
            strncat(output, " ", out_size - strlen(output) - 1);
        }
    }
}

// --- ONNX Runtime Inference ---

int main()
{
    const OrtApi *api = OrtGetApiBase()->GetApi(ORT_API_VERSION);
    OrtEnv *env = NULL;
    OrtSessionOptions *session_options = NULL;
    OrtSession *session = NULL;
    OrtAllocator *allocator = NULL;

    // Create environment
    api->CreateEnv(ORT_LOGGING_LEVEL_WARNING, "inference", &env);
    // Create session options and set number of threads and optimization level
    api->CreateSessionOptions(&session_options);
    api->SetIntraOpNumThreads(session_options, 1);
    api->SetSessionGraphOptimizationLevel(session_options, ORT_ENABLE_ALL);

    // Create session from the ONNX model file (assumed exported as transformer.onnx)
    const char *model_path = "transformer.onnx";
    api->CreateSession(env, model_path, session_options, &session);

    // Get a default allocator
    api->GetAllocatorWithDefaultOptions(&allocator);

    // Retrieve input name (assuming one input)
    char *input_name = NULL;
    api->SessionGetInputName(session, 0, allocator, &input_name);

    // For simplicity, assume the output node is named "output"
    const char *output_names[] = {"output"};

    // Main interactive loop for inference
    char input_text[256];
    printf("Enter input text (or 'quit' to exit):\n");
    while (fgets(input_text, sizeof(input_text), stdin))
    {
        if (strncmp(input_text, "quit", 4) == 0)
            break;

        int input_ids[MAX_SEQ_LEN] = {0};
        int seq_len = tokenize(input_text, input_ids, MAX_SEQ_LEN);
        if (seq_len <= 0)
        {
            printf("No valid tokens. Try again.\n");
            continue;
        }

        // Define input tensor shape [1, seq_len]
        int64_t dims[2] = {1, seq_len};
        size_t input_tensor_size = seq_len;

        // Create a tensor from the input data
        OrtMemoryInfo *memory_info = NULL;
        api->CreateCpuMemoryInfo(OrtArenaAllocator, OrtMemTypeDefault, &memory_info);
        OrtValue *input_tensor = NULL;
        api->CreateTensorWithDataAsOrtValue(
            memory_info,
            input_ids,
            input_tensor_size * sizeof(int),
            dims,
            2,
            ONNX_TENSOR_ELEMENT_DATA_TYPE_INT32,
            &input_tensor);
        api->ReleaseMemoryInfo(memory_info);

        // Run the session (for simplicity, using default run options)
        OrtValue *output_tensor = NULL;
        api->Run(session,
                 NULL,
                 &input_name,
                 (const OrtValue *const *)&input_tensor,
                 1,
                 output_names,
                 1,
                 &output_tensor);

        // Get pointer to output data (assume output tensor is int32 and shape [1, out_seq_len])
        int *output_data = NULL;
        api->GetTensorMutableData(output_tensor, (void **)&output_data);

        // Retrieve output tensor shape info
        OrtTensorTypeAndShapeInfo *output_info = NULL;
        api->GetTensorTypeAndShape(output_tensor, &output_info);
        size_t num_dims;
        api->GetDimensionsCount(output_info, &num_dims);
        int64_t *out_dims = malloc(num_dims * sizeof(int64_t));
        api->GetDimensions(output_info, out_dims, num_dims);
        int out_seq_len = (num_dims >= 2) ? (int)out_dims[1] : 0;
        free(out_dims);
        api->ReleaseTensorTypeAndShapeInfo(output_info);

        // Detokenize output tokens into a string
        char output_text[512];
        detokenize(output_data, out_seq_len, output_text, sizeof(output_text));
        printf("Generated Output: %s\n", output_text);

        api->ReleaseValue(output_tensor);
        api->ReleaseValue(input_tensor);

        printf("Enter input text (or 'quit' to exit):\n");
    }

    // Clean up
    api->AllocatorFree(allocator, input_name);
    api->ReleaseSession(session);
    api->ReleaseSessionOptions(session_options);
    api->ReleaseEnv(env);

    return 0;
}
