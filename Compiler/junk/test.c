#include <stdio.h>
#include <string.h>

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
    // char instring[];
    // strcpy(instring, input);
    // char space[]=" ";
    // char *tok;
    // tok=strtok(instring, space);
    // while(tok!=NULL) {printf("%s\n",tok); tok=strtok(NULL, space);}
    // fgets(input, sizeof(code),code);
    fscanf(code, "%s", input);
    printf(input);
}}