#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_TEXT_LENGTH 100
#define MAX_WHOLE_LENGTH 10
#define MAX_DECIMAL_LENGTH 10
#define MAX_LIT_LENGTH 5
#define TRUE 1
#define FALSE 0

typedef enum{
    TOKEN_IDENTIFIER,
    TOKEN_LITERAL,
    TOKEN_OPERATOR,
    TOKEN_KEYWORD,
    TOKEN_DELIMETER,
    TOKEN_COMMENT,
    TOKEN_TEXT,
    TOKEN_WHOLE,
    TOKEN_DECIMAL,
    TOKEN_LIT,
    TOKEN_UNKOWN
}TokenTypes;

typedef struct{
    TokenTypes type;
    char *value;
}Token;   

typedef struct{
    Token token;
    struct Node *next;
} Node;

#define NUM_KEYWORDS 27
#define NUM_OPERATORS 33
#define NUM_DELIMETERS 9

const char *reserved[]={   "text", "whole", "dec", "seq", "lit", "blank", "sheesh", "bruh", "steady", "tas", 
    "or", "deins", "kung", "ehkung", "edi", "choice", "when", "go", "habang", "for", "to", 
    "step", "termins", "gg", "use", "from", "as"
    };

const char *operators[]={  "=", "+=", "-=", "*=", "/=", "%%=", "==", ">", ">=","<", "<=", "!=", "+", "-", "*", "/", "%%"  };
const char *symbols[]={"#", "[", "]", "{", "}", "(", ")", ",", "/*", "*/", "//", """, """,".", ":", "::", "\n"};
const char *delimeters[]={" ", "#", "(", ")", "\n", "{","}", "!", "[","]", "-", ","};

const char* split(char *code){
    // Node *head=malloc(sizeof(Node));
    // Node *next;
    // Node *tail;

    char *token;
    char *tokens;
    int i=0;
    tokens=(char*)malloc(sizeof(char)*strlen(code));
    while(!strtok(code, delimeters[i])){
        if(strtok(code, delimeters[i])){
        token=strtok(code, delimeters[i]);
        break;
        }
        i++;

    }
    
    while(token!=NULL){
        printf("%s\n", token);
        token=strtok(NULL, delimeters);
        tokens[i]=token;
    }
    return tokens;


}
Token tokenize(char *str);
const char *isIdentifier(char *str);
const char *isLiteral(char *str);
const char *isOperator(char *str);

Token isKeyword(char *kw){
    Token keyword;
    for(int i=0; i<sizeof(reserved); i++){
        if(strcmp(kw, reserved[i])==0){
            keyword.type=TOKEN_KEYWORD;
            strcpy(keyword.value, kw);
            return keyword;
        }
    }
}
const char *isDelimiter(char *str);
const char *isComment(char *str);
const char *isText(char *str);
const char *isWhole(char *str);
const char *isDecimal(char *str);
const char *isLit(char *str);
//Function which removes all non-delimeter whitespace characters
const char* removeSpace(char *str);

int main(){
char *tokenize;
char *input;

long length;
FILE *code = fopen("C:\\Users\\anton\\Desktop\\input.txt", "r");
if(code){
    fseek(code, 0, SEEK_END);
    length=ftell(code);
    fseek(code, 0, SEEK_SET);
    input=(char*)malloc(length);
    if(input){
        fread(input, 1, length, code);    
    }
    fclose(code);
}

if(input){
//     tokenize=split(input);
//     while(code!= NULL){
//     printf(tokenize);
// }
    char tok[sizeof(input)];
    strcpy(tok, input);
    char delim[]=" ";
    char* out=strtok(tok, delim);
    while(tok!=" "){
    printf(" %s\n", out); 
    out=strtok(NULL, delim);
    }
}

return 0;
}