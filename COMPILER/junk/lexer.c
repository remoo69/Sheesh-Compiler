#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define MAX_TOKEN_LENGTH 100

// Define token types
typedef enum {
    TOKEN_IDENTIFIER,
    TOKEN_NUMBER,
    TOKEN_OPERATOR,
    TOKEN_KEYWORD,
    TOKEN_DELIMITER,
    TOKEN_STRING_LITERAL,
    TOKEN_COMMENT,
    TOKEN_UNKNOWN
} TokenType;

// Define token structure
typedef struct {
    TokenType type;
    char value[MAX_TOKEN_LENGTH];
} Token;

// Define keyword list
const char *keywords[] = {
    "text", "whole", "dec", "seq", "lit", "blank", "sheesh", "bruh", "steady", "tas", 
    "or", "deins", "kung", "ehkung", "edi", "choice", "when", "go", "habang", "for", "to", 
    "step", "termins", "gg", "use", "from", "as"
};
const int num_keywords = sizeof(keywords) / sizeof(keywords[0]);

// Define operator list
const char *operators[] = {
    "+", "-", "*", "/", "%", "++", "--", "==", "!=", ">", "<", ">=", "<=",
    "&&", "||", "!", "&", "|", "^", "~", "<<", ">>", "=", "+=", "-=", "*=",
    "/=", "%=", "<<=", ">>=", "&=", "^=", "|="
};
const int num_operators = sizeof(operators) / sizeof(operators[0]);

// Define delimiter list
const char *delimiters[] = {
    "(", ")", "{", "}", "[", "]", ",", ";", ":"
};
const int num_delimiters = sizeof(delimiters) / sizeof(delimiters[0]);

// Function to check if a string is a keyword
int is_keyword(char *str) {
    for (int i = 0; i < num_keywords; i++) {
        if (strcmp(str, keywords[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

// Function to check if a string is an operator
int is_operator(char *str) {
    for (int i = 0; i < num_operators; i++) {
        if (strcmp(str, operators[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

// Function to check if a string is a delimiter
int is_delimiter(char *str) {
    for (int i = 0; i < num_delimiters; i++) {
        if (strcmp(str, delimiters[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

// Function to get the next token from the input stream
Token get_token(FILE *input) {
    Token token = {TOKEN_UNKNOWN, ""};
    char c = fgetc(input);

    // Skip whitespace
    while (isspace(c)) {
        c = fgetc(input);
    }

    // Handle identifiers and keywords
    if (isalpha(c) || c == '_') {
        int i = 0;
        while (isalnum(c) || c == '_') {
            token.value[i++] = c;
            c = fgetc(input);
        }
        token.value[i] = '\0';
        if (is_keyword(token.value)) {
            token.type = TOKEN_KEYWORD;
        } else {
            token.type = TOKEN_IDENTIFIER;
        }
        ungetc(c, input);
    }

    // Handle numbers
    else if (isdigit(c)) {
        int i = 0;
        while (isdigit(c)) {
            token.value[i++] = c;
            c = fgetc(input);
        }
        if (c == '.') {
            token.value[i++] = c;
            c = fgetc(input);
            while (isdigit(c)) {
                token.value[i++] = c;
                c = fgetc(input);
            }
        }
        token.value[i] = '\0';
        token.type = TOKEN_NUMBER;
        ungetc(c, input);
    }

    // Handle operators
    else if (is_operator(&c)) {
        int i = 0;
        token.value[i++] = c;
        if (c == '+' || c == '-' || c == '&' || c == '|') {
            char next = fgetc(input);
            if (next == c) {
                token.value[i++] = next;
            } else {
                ungetc(next, input);
            }
        } else if (c == '<' || c == '>') {
            char next = fgetc(input);
            if (next == c || next == '=') {
                token.value[i++] = next;
            } else {
                ungetc(next, input);
            }
        } else if (c == '=') {
            char next = fgetc(input);
            if (next == '=') {
                token.value[i++] = next;
            } else {
                ungetc(next, input);
            }
        }
        token.value[i] = '\0';
        token.type = TOKEN_OPERATOR;
    }

    // Handle delimiters
    else if (is_delimiter(&c)) {
        token.value[0] = c;
        token.value[1] = '\0';
        token.type = TOKEN_DELIMITER;
    }

    // Handle string literals
    else if (c == '\"') {
        int i = 0;
        token.value[i++] = c;
        c = fgetc(input);
        while (c != '\"' && c != EOF) {
            token.value[i++] = c;
            c = fgetc(input);
        }
        token.value[i++] = c;
        token.value[i] = '\0';
        token.type = TOKEN_STRING_LITERAL;
    }

    // Handle comments
    else if (c == '/') {
        char next = fgetc(input);
        if (next == '/') {
            while (c != '\n' && c != EOF) {
                c = fgetc(input);
            }
            ungetc(c, input);
            token.type = TOKEN_COMMENT;
        } else if (next == '*') {
            char prev = ' ';
            while ((prev != '*' || c != '/') && c != EOF) {
                prev = c;
                c = fgetc(input);
            }
            token.type = TOKEN_COMMENT;
        } else {
            ungetc(next, input);
            token.value[0] = c;
            token.value[1] = '\0';
            token.type = TOKEN_OPERATOR;
        }
    }

    // Handle end of file
    else if (c == EOF) {
        token.type = TOKEN_UNKNOWN;
    }

    // Handle unknown characters
    else {
        token.value[0] = c;
        token.value[1] = '\0';
        token.type = TOKEN_UNKNOWN;
    }

    return token;
}

// Main function
int main() {
    FILE *input = fopen("C:\\Users\\anton\\Desktop\\input.txt", "r");
    Token token = get_token(input);
    while (token.type != TOKEN_UNKNOWN) {
        printf("%s: %s\n", token.value, token.type == TOKEN_UNKNOWN ? "unknown" :
            token.type == TOKEN_IDENTIFIER ? "identifier" :
            token.type == TOKEN_NUMBER ? "number" :
            token.type == TOKEN_OPERATOR ? "operator" :
            token.type == TOKEN_KEYWORD ? "keyword" :
            token.type == TOKEN_DELIMITER ? "delimiter" :
            token.type == TOKEN_STRING_LITERAL ? "string literal" :
            token.type == TOKEN_COMMENT ? "comment" : "unknown");
        token = get_token(input);
    }
    fclose(input);
    return 0;
}
