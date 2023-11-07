#Prepares the Input file for tokenization. Removes comments, extra newline characters, and extra spaces.
#Also splits the code into lines.
import constants as const
import re
import lexerpy as lex

def file_to_string(file):
    try:
        with open(file, "r") as f:
            data = f.read()
        return data
    except FileNotFoundError:
        print("File not found.")
        return None

def remove_comments(code):
    # Remove block comments
    code = re.sub(const.RE_BlockComment, '', code, flags=re.DOTALL)
    # Remove inline comments
    code = re.sub(const.RE_InlineComment, '\n', code)
    return code
    
def remove_whitespace_type(tokens, category):
    new_tokens = []
    new_category = []
    for i in range(len(tokens)):
        if category[i] != "Whitespace":
            new_tokens.append(tokens[i])
            new_category.append(category[i])
    return new_tokens, new_category

def getlines(code):
    #Splits the code into lines
    lines=[]
    lines=code.split("\n")
    return lines

def get_delim_key(delim_char):
    for key, value in const.delimiters.items():
        if delim_char in value:
            return key
    return None

# def get_delim(token):
#     pass


def get_whole(token):
    token_cpy=''
    temp_token=''

    for char in token:
        if char is None:
            return '',token
        if char in const.delimiters["n_delim"] and lex.is_Whole(temp_token):
            token_cpy=re.sub(temp_token, '',token, count=1)
            return temp_token, token_cpy       
        else:
            temp_token+=char
    
def get_dec(token):
    token_cpy=''
    temp_token=''
    dec_detected=False
    for char in token:
        if char in const.delimiters["n_delim"] and lex.is_Dec(temp_token):
            token_cpy=re.sub(re.escape(temp_token), '',token, count=1)
            return temp_token, token_cpy       
        else:
            temp_token+=char

# def get_lit(token):
#     if get_keyword(token)==const.boolean:
#         return 

def get_keyword(token):
    token_cpy=''
    temp_token=''
    keyword_detected=False
    for char in token:
        if temp_token is None:
            return '',token
        if temp_token in const.keywords and char in const.keywords_delims[temp_token]:
            token_cpy=re.sub(temp_token, '',token, count=1)
            keyword_detected=True
            return temp_token, token_cpy       
        else:
            temp_token+=char
   
def get_identifier(token):
    token_cpy=''
    temp_token=''
    for char in token:
        if char in const.delimiters["id_delim"] and lex.is_Identifier(temp_token):
            token_cpy=re.sub(temp_token, '',token, count=1)
            return temp_token, token_cpy       
        else:
            temp_token+=char

    
    
def get_symbol(token):
    token_cpy=''
    next_temp=''
    for i, char in enumerate(token):
         if char in const.symbols:
            try:                    
                # n =#
                next_temp = char + token[i + 1]
                next_next_temp = str(next_temp + token[i + 2])
            except IndexError:
                next_temp += char
                next_next_temp = ''
            if next_next_temp=="...":
                if token[i+3] not in const.symbols_delims[next_next_temp]:
                    return None
                token_cpy = re.sub(re.escape(next_next_temp), '', token, count=1)
                return next_next_temp, token_cpy    
            elif next_temp in const.compound_symbols:
                if token[i+2] not in const.symbols_delims[next_temp]:
                    return None
                token_cpy = re.sub(re.escape(next_temp), '', token, count=1)
                return next_temp, token_cpy
            else:
                # if len(token)==1 and lex.is_Symbol(token):
                #     return token, None
                # if token[i+1] not in const.symbols_delims[char] :
                #     return None
                token_cpy = re.sub(re.escape(char), '', token, count=1)
            return char, token_cpy
         else:
            return None
            

def get_space(token):
    token_cpy=''
    temp_token=''
    space_detected=False
    space=r'\s'
    for char in token:
        if re.match(space, char):
            token_cpy=re.sub(space, '',token, count=1)
            return char, token_cpy       
    
def get_text(token):
    #Returns the text token and the remaining code
    token_cpy=''
    temp_token=''
    text_detected=False
    for i,char in enumerate(token):
        try:
            check_concat=char+token[i+1]+token[i+2]
        except IndexError:
            check_concat=''
        if (char in const.delimiters["txt_delim"] or check_concat=="...") and lex.is_Text(temp_token):
            token_cpy=re.sub(temp_token, '',token, count=1)
            return temp_token, token_cpy       
        else:
            temp_token+=char

def get_next_char(input_string, current_index):
    if current_index < len(input_string)-1:
        return input_string[current_index+1]
    else:
        return None
        


def gettokens(code):
    # Iterate through a line of code per character and return as a list of tokens
    # Check each character
    tokencode = code
    tokens = []
    current_token:str = ''
    tktype = ''

    while tokencode:
        if get_keyword(tokencode):
            result=get_keyword(tokencode)
            if result is not None:
                current_token, tokencode = result
            else: continue
            tktype = "keyword"
        elif get_identifier(tokencode):
            result=get_identifier(tokencode)
            if result is not None:
                current_token, tokencode = result
                
            else: continue
            tktype = "identifier"
        elif get_text(tokencode):
            result=get_text(tokencode)
            if result is not None:
                current_token, tokencode = result
            else: continue
            tktype = "text"
        elif get_dec(tokencode):
            result=get_dec(tokencode)
            if result is not None:
                current_token, tokencode = result
            else: continue
            tktype = "dec"
        elif get_whole(tokencode):
            result=get_whole(tokencode)
            if result is not None:
                current_token, tokencode = result
            else: continue
            tktype = "whole"
        elif get_symbol(tokencode):
            result=get_symbol(tokencode)
            if result is not None:
                current_token, tokencode = result
            else: continue
            tktype = "symbol"
        else:
            print(f"may pumasok dito tc:{tokencode} ct:{current_token} t:{tokens}")
            if tokencode:
                print("outerif")
                if current_token is None or current_token=='':
                    print("interrif")
                    current_token=tokencode
                    tokens.append(tokencode)
                    tokencode=None
                    tokens.append(None)
                    break
            # if current_token[-1]
        #    print(f"pasok sa else par {current_token}, {tokencode}, {tokens}")
        #    current_token=tokencode
        #    tokencode=None
        #    if current_token is None or current_token=='' or current_token==' ':
        #        print("pumasok sa if")
        #        error=lex.error_handler(None, tokens, None)
        #        print(error)
        #    else:
        #     # print("Else loob gettokens")
        #     # category=lex.categorize(current_token)
        #     # error=lex.error_handler(current_token, tokens, tokencode)
        #     # print(error," for ", current_token)
        #     print(f"Pumasok sa else, {tokencode} {current_token} ")
        #     tokens.append(current_token)
        #     current_token=''
        
            
            
            else:
                print("else labas")
                tokens.append("None")
                break
            
        
        if current_token:
                tokens.append(current_token)
                current_token = ''
        else: #Handles null chars
            print("Else labas gettokens")
            error=lex.error_handler(None, tokens, None)
            print(error, "for", current_token)
    return tokens

def prepare(code):
#Prepares the code for tokenization. Removes comments, extra newline characters, and extra spaces.
# Returns each line of code as a list of strings; ignores empty lines.
    templines=getlines(remove_comments(code))
    lines=[] 
    for i in range(len(templines)):
        # if templines[i]=="": #Skips empty lines
        #     continue
        lines.append(templines[i])
    return lines
