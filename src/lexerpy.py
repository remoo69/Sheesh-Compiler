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

# def is_Lit(Token):
#     if Token in const.boolean:
#         return True
#     else:
#         return False    

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
def is_Symbol(Token):
    if Token in const.symbols or Token in const.concat:
        return True
    else:
        return False

def is_Keyword(Token):
    if Token in const.keywords:
        return True
    else: return False       

# def tokenize(code):
#    #Takes prepared code in lines and tokenizes each line. stores each token as an object
#    for line in code:
#          for token in line:
#               i=0
#               if is_Text(token):
#                 return tk.Token(value=token, type="text", attribute="text", line=line)
#               elif is_Whole(token):
#                 return tk.Token(value=token, type="whole", attribute="whole")
#               elif is_Dec(token):
#                 return tk.Token(value=token, type="dec", attribute="dec")
#             #   elif is_Lit(token):
#             #     return tk.Token(value=token, type="lit", attribute="lit")
#               elif keyword_type(token, token[i]):
#                 return tk.Token(value=token, type="keyword", attribute="keyword")
#               elif is_Identifier(token):
#                 return tk.Token(value=token, type="identifier", attribute="identifier")
#               elif is_Delimiter(token):
#                 return tk.Token(value=token, type="delimiter", attribute="delimiter")
#               else:
#                 return tk.Token(value=token, type="error", attribute="error")

def categorize(lexeme):
    #Categorizes each token based on their type and attribute
    #Takes a list of tokenized lines
    if is_Keyword(lexeme):
        return "Keyword"
    elif is_Identifier(lexeme):
        return "Identifier"
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
        pass
    else:
        return "Error Category"
            
    
def error_handler(current, tokenized):
    error_val = current
    token_prev = tokenized[-1]
    category = categorize(token_prev)
    # This portion is for delimiter mismatches
    if current is None or token_prev is None or current.isspace():
        return "Invalid Null Delimiter"

    # Categorize previously matched token
    

    # Check if the delimiter is valid for the token category
    if category == "Keyword":
        if error_val not in const.keywords_delims[tokenized[-1]]:
            return f"Invalid Delimiter for {category}"
    elif category == "Identifier":
        if error_val not in const.delimiters["id_delim"]:
            return f"Invalid Delimiter for {category}"
    elif category == "Symbol":
        if error_val not in const.symbols_delims[tokenized[-1]]:
            return f"Invalid Delimiter for {category}"
    elif category == "Text":
        if error_val not in const.delimiters["text_delim"]:
            return f"Invalid Delimiter for {category}"
    elif category in ["Whole", "Dec"]:
        if error_val not in const.delimiters["n_delim"] :
            return f"Invalid Delimiter for {category}"
    elif category == "Error Category":
        if error_val not in const.keywords_delims[tokenized[-1]]:
            return f"Invalid Delimiter for {category}"
    # if category=="Keyword":
    #     if error_val not in const.keywords_delims[tokenized[-1]]:
    #         return f"Invalid Delimiter for {category}"
            
    # elif category=="Identifier":
    #     if error_val not in const.delimiters["id_delim"]:
    #         return f"Invalid Delimiter for {category}"
    # elif category=="Symbol": #pano gagawin ko dito tf
    #     # if error_val not in const.keywords_delims[tokenized[len(tokenized)-1]]:
    #     #     remaining=re.sub(re.escape(error_val), '',remaining, count=1)
    #     #     return f"Invalid Delimiter for {category}", remaining
    #     if error_val[0] not in const.symbols_delims[tokenized[len(tokenized)-1]]:
    #         return f"Invalid Delimiter for {category}"
        
    # elif category=="Text":
    #     if error_val not in const.delimiters["text_delim"]:
    #         return f"Invalid Delimiter for {category}"
    # elif category=="Whole":
    #     if error_val not in const.delimiters["n_delim"]:
    #         return f"Invalid Delimiter for {category}"
    # elif category=="Dec":
    #     if error_val not in const.delimiters["n_delim"]:
    #         return f"Invalid Delimiter for {category}"
    # elif category=="Error Category": #This portion should handle if the previous token is also not a valid token
    #     if error_val not in const.keywords_delims[tokenized[len(tokenized)-1]]:
    #         return f"Invalid Delimiter for {category}"
    else: #if not delim error, then could be token syntax error. 
        return "Invalid Token Syntax"
    # print("Error: " + error + " at line " + str(line) + ", position " + str(position) + "."
    # if current is not None:
    #     print(f"Error at {current}")
    #     remaining=re.sub(re.escape(current), '',remaining, count=1)
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
