import re
import pandas as pd
from tabulate import tabulate
DATA_TYPES=["text", "whole", "dec", "lit", "void"]
RE_Literals={"text": r'^\"(?:(?:(?!(?<!\\)").) | (?:\\"))*$\"',
              "whole": r'\d+', 
              "dec": r'\d+\.\d+', 
              "lit": r'(True|False)'}

RE_Identifier=r'[a-zA-Z_][a-zA-Z0-9_]{0,28}$'

keywords = [ "text", "whole", "dec", "seq", "lit", "blank", "sheesh", "bruh", "steady", "tas", 
    "or", "deins", "kung", "ehkung", "edi", "choice", "when", "go", "habang", "for", "to", 
    "step", "termins", "gg", "use", "from", "as"]
operators = [ "=", "+=", "-=", "*=", "/=", "%%=", "==", ">", ">=","<", "<=", "!=", "+", "-", "*", "/", "%%" ]
symbols = ["#", "[", "]", "{", "}", "(", ")", ",", "/*", "*/", "//", """, """,".", ":", "::", "\n", " "]

WHOLE_MIN=-32768
WHOLE_MAX=32767
DEC_MIN=-32768.999999
DEC_MAX=32767.999999

class Token:
    def __init__(self, type=None, value=None, line=None, position=None, quality=None):
        self.type = type
        self.value = value
        self.line = line
        self.position = position
        self.quality=quality

def file_to_string(file):
    with open(file, "r") as f:
        data = f.read()
    return data

def remove_comments(code):
    # Remove block comments
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    # Remove inline comments
    code = re.sub(r'//.*?\n', '\n', code)
    return code

def remove_spaces(code):
    # Remove spaces
    code = re.sub(r'\s+', '', code)
    return code

def check_token_consistency(code: str):
    if re.match(RE_Identifier, code):
        return "Identifier"
    elif re.match(RE_Literals["text"], code):
        return "Text"
    elif code.isdigit():
        return "Digit"
    elif code in operators:
        return "Operator"
    elif code in symbols:
        return "Symbol"
    else:
        return "Mix"
def prepare(code):
#Prepares the code for tokenization. Removes comments, newline characters, and spaces after the terminator.
#Also places each token in a list.   
    lines=[]
    tokens=[]
    code=remove_comments(code)
    lines=code.split("\n") #Splits the code into lines
    for i in range(len(lines)):
        if lines[i]=="": #Skips empty lines
            continue
        tokens=tokens+lines[i].split() #Splits each line into words
    return tokens



    
def is_Text(Token):
    return re.match(RE_Literals["Text"], Token)


def tokenize(code):
   

    tokens = []
    lines = code.split('\n')
    for i, line in enumerate(lines):
        words = line.split()
        position = 0
        for word in words:
            if word in keywords:
                tokens.append(Token('keyword', word, i+1, position+1))
            elif word in operators:
                tokens.append(Token('operator', word, i+1, position+1))
            elif word in symbols:
                tokens.append(Token('separator', word, i+1, position+1))
            elif word.isdigit():
                tokens.append(Token('number', int(word), i+1, position+1))
            elif word.isalpha():
                tokens.append(Token('identifier', word, i+1, position+1))
            # else:
            #     raise ValueError(f"Invalid token '{word}' at line {i+1}, position {position+1}")
            position += len(word) + 1
    return tokens

    


def main():
    code = file_to_string(r"C:\Users\anton\Desktop\input1.sheesh")
    # tokens = tokenize(code)
    # for token in tokens:
    # print(remove_spaces(remove_comments(code)))
    prepcode=prepare(code)
    tags=[]
    # print(prepcode)
    for i in range(len(prepcode)):
        tags.append(check_token_consistency(prepcode[i]))

    data={"Token": prepcode, "Tag": tags}
    df=pd.DataFrame(data)
 
    print(tabulate(df, headers='keys', tablefmt='psql'))
    print(re.match(RE_Identifier, "zzz===5"))

main()
