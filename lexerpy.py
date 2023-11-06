import re
import tokenclass as tk
import pandas as pd
from tabulate import tabulate
import constants as const
import prepare as prep
import tokenclass as tk

# This lexer follows the principle of longest match. It will match the longest possible token at each step.

# Say for example that a token dec15# is passed. The lexer will detect the token line by line until a delimiter is found. Thus, 
# Even if dec is a reserved word, the lexer will not detect it as such because it will be detected as an identifier due to the delimiter # being after the 15 value.
# If dec were to be used as a keyword, the syntax should be: dec identifier=15#. Here, dec is detected as a keyword due to the delimiter {space}

# Each function checks if a token is within a valid token type based on their respective regular expressions and delimiters.
# As such, the delimiter of the token should be passed along with the token itself. Do note that the delimiter itself should be considered a token.

# Update: Let the inputs be a list of tokens per line. This way the lexer can check each token while keeping track of its delimiter while not having to include the delimiter itself in the detection.
# This is so the lexer can detect the token type of the delimiters themselves.
def is_Text(Token)->bool:
    #Checks if a token has a valid delimiter for a text literal; returns true if all rules and conditions are met.
    if re.match(const.RE_Literals["text"], Token):
        return True
    else:
        return False

def is_Identifier(Token):
    if re.match(const.RE_Identifier, Token):
        return True
    else:
        return False
    
def is_Whole(Token):
    if re.match(const.RE_Literals["whole"], Token):
        return True
    else:
        return False

def is_Dec(Token):
    if re.match(const.RE_Literals["pos_dec"], Token) or re.match(const.RE_Literals["neg_dec"], Token):
        return True
    else:
        return False

   

#Needs further work
def keyword_type(Token, delimiter):
    #This function already returns the tokentype, 
    for i in const.keywords:
        pass
        # if Token==and delimiter in const.delimiters["delim3"]:
        # return True

        # else:
        #     return False

#Might run into problems here because delimiters include characters as well, not just symbols
def is_Operator(Token):
    if Token in const.all_op:
        return True
    else:
        return False
    
def is_Symbol(Token):
    if Token in const.non_op:
        return True
    else:
        return False

def is_Keyword(Token):
    if Token in const.keywords:
        return True
    else: return False       

def is_Numeric(Token):
    if is_Whole(Token) or is_Dec(Token):
        return True
    else: return False


def categorize(lexeme:str):
    #Categorizes each token based on their type and attribute
    #Takes a list of tokenized lines
    if is_Keyword(lexeme):
        return "Keyword"
    elif is_Identifier(lexeme) and len(lexeme)<=9:
        return "Identifier"
    elif is_Operator(lexeme):
        return "Operator"
    elif is_Symbol(lexeme):
        return "Symbol"
    elif is_Text(lexeme):
        return "Text"
    elif is_Whole(lexeme):
        return "Whole"
    elif is_Dec(lexeme):
        return "Dec"
    elif lexeme in const.boolean:
        return "Lit"
    elif lexeme is None:
        print("lex is none")
    elif lexeme in const.whitespace:
        return "Whitespace"
    else:
        return "Error Category"
            
    
def error_handler(current, tokenized, remaining):
    error_val = current
    try:
        if current=='' or current is None:
            return f"Type 1 Invalid Null Delimiter for \"{tokenized[-1]}\", remaining: {remaining}"
        # This portion is for delimiter mismatches
        if remaining is None and not is_Symbol(error_val):
            return f"Type 2 Invalid Null Delimiter for \"{current}\""

        if is_Identifier(error_val) and len(error_val)>9:
            return f"Type 3 Identifier {error_val} contains legal characters but is too long "
        # Categorize previously matched token
        token_prev = tokenized[-1]
        category = categorize(token_prev)

        # Check if the delimiter is valid for the token category (prev)
        if category == "Keyword":
            if error_val not in const.keywords_delims[tokenized[-1]]:
                return f"Invalid Delimiter for \"{category}\", \"{token_prev}\""
        elif category == "Identifier":
            if error_val not in const.delimiters["id_delim"]:
                return f"Invalid Delimiter for \"{category}\", \"{token_prev}\""
        elif category == "Error Category":
            if error_val not in const.keywords_delims[tokenized[-1]]:
                return f"{error_val} Invalid Syntax for Token"
        elif category == "Symbol":
            if not is_Numeric(error_val) and not is_Identifier(error_val) and not is_Operator(error_val):
                return f"{error_val} Invalid Delimiter for \"{category}\", \"{token_prev}\""
        elif category == "Operator":
            if error_val not in const.delimiters["op"]:
                return f"Invalid Delimiter for \"{category}\", \"{token_prev}\""
        elif category == "Text":
            if error_val not in const.delimiters["txt_delim"] and error_val not in const.concat:
                return f"Invalid Delimiter for \"{category}\", \"{token_prev}\""
        elif category in ["Whole", "Dec"]:
            if error_val not in const.delimiters["n_delim"] :
                return f"Invalid Delimiter for \"{category}\", \"{token_prev}\""
        elif category=="Whitespace":
            if error_val not in const.delimiters["space_delim"] or categorize(error_val) not in const.valid_tokens:
                return f"Invalid Delimiter for \"{category}\", \"{token_prev}\""

        
        else: #if not delim error, then could be token syntax error. 
            return "Invalid Token Syntax"
        
    except IndexError:
        return "Invalid Delimiter and Statement"
    

def tokenize(codes):
    lines = prep.prepare(codes)
    tokens=[]
    category=[]
    error=[]
    for i,line in enumerate(lines):
        lexeme=prep.gettokens(line)
        for j,token in enumerate(lexeme):
            if token is None or categorize(token) not in const.valid_tokens:
                print(token,"errcat")
                errortype=error_handler(token, tokens, lexeme[j+1:])
                error.append(f"Line {i+1}: {errortype}")
            else:
                tokens.append(token)
                category.append(categorize(token))
            
            # elif 

            
    
    # error=error_handler
    return tokens, category, error



# def main():
#     code = prep.file_to_string(r"C:\Users\anton\Desktop\input1.sheesh")
#     tokens = prep.prepare(code)
#     tokenized=tokenize(tokens)
#     # tokens_dict = {token.value: token.quality for token in tokens}
#     # df = pd.DataFrame(tokens_dict.items(), columns=['Token', 'Tag'])
#     # print(tabulate(df, headers='keys', tablefmt='psql'))
#     print(tokens)
#     print(tokenized)

# main()
