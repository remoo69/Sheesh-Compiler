import constants as const
import re
import lexerpy as lex
def gettokens(code):
    tokencode=code
    # delimiters=[val for sublist in const.delimiters.values() for val in sublist]
    # delimiters=list(dict.fromkeys(delimiters))
    # tokens = []
    # current_token = ''
    # for char in code:
    #     if char in delimiters:
    #         if current_token:
    #             tokens.append(current_token)
    #             current_token = ''
    #     else:
    #         current_token += char
    #     current_token=current_token+char
    # if current_token:
    #     tokens.append(current_token)

    # return tokens
    tokens=[]
    current_token=''
    for char in tokencode:
        #if token is literal:
        if char in const.delimiters["txt_delim"] and current_token.lex.is_Text():
            tokens.append(current_token)
            re.sub(current_token, tokencode, '', count=1)
            current_token=''
        #if token is whole:
        elif char in const.delimiters["n_delim"] and current_token.lex.is_Whole():
            tokens.append(current_token)
            re.sub(current_token, tokencode, '', count=1)
            current_token=''

        #if token is decimal:
        elif char in const.delimiters["n_delim"] and current_token.lex.is_Dec():
            tokens.append(current_token)
            re.sub(current_token, tokencode, '', count=1)
            current_token=''

        #if token is 

        if char in const.symbols:
            if current_token:
                tokens.append(current_token)
                re.sub(current_token, tokencode, '', count=1)
                current_token=''
        elif char in const.delimiters["delim1"]:
            tokens.append(current_token)
            re.sub(current_token, tokencode, '', count=1)
            current_token=''
        current_token+=char

        #If token is keyword

        #If token is identifier

        #If token is operator

        #If token is delimiter
    return tokens