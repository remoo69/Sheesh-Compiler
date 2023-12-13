#from: prepare.py

# # def remove_spaces(code):    
# #     # Remove spaces
# #     code = re.sub(r'\s+', '', code)
# #     return code

# # def check_token_consistency(code: str):
# #     if code in const.keywords:
# #         return "Keyword"
# #     elif re.match(const.RE_Identifier, code):
# #         return "Identifier"
# #     elif re.match(const.RE_Literals["text"], code):
# #         return "Text"
# #     elif code.isdigit():
# #         return "Digit"
# #     elif code in const.op:
# #         return "Operator"
# #     elif code in const.symbols:
# #         return "Symbol"
# #     else:
# #         check_token_consistency(splitmore(code))
    

# # def splitmore(code):
# #     #splits a compound token into smaller tokens
# #     token=[]
# #     tokens=[]
# #     for i in code:
# #         token.append(i)
# #         jointoken="".join(token)    
# #         if check_token_consistency(jointoken)==True:
# #             token.clear()
# #             jointoken=""
            
#    # return token
# def resplit(token):
#     final = []
#     res = []
#     while token!=None:
#         for chars in token:  
#             res.append(chars)     
#             tok1 = "".join(res)
#             if tok1 in const.keywords:
#                 final.append(tok1)
#                 print("Keyword")
#                 re.sub(tok1, '', token)
#                 break
            
#             else:
#                 if re.match(const.RE_Identifier, tok1):
#                     final.append(tok1)
#                     print("Identifiers")
#                     re.sub(tok1, '', token)
#                     break
#                 elif re.match(const.RE_Literals["text"], tok1):
#                     final.append(tok1)
#                     re.sub(tok1, '', token)
#                     break
#                 elif tok1.isdigit():
#                     final.append(tok1)
#                     re.sub(tok1, '', token)
#                     break
#                 elif tok1 in const.op:
#                     final.append(tok1)
#                     re.sub(tok1, '', token)
#                     break
#                 elif tok1 in const.symbols:
#                     final.append(tok1)
#                     re.sub(tok1, '', token)
#                     break
#     # Check for a valid token in the remaining characters
#     # if res:
#     #     tok1 = "".join(res)
#     #     if tok1 in const.keywords or tok1 in const.op or tok1 in const.symbols or tok1.isdigit() or re.match(const.RE_Identifier, tok1) or re.match(const.RE_Literals["text"], tok1):
#     #         final.append(tok1)
#     return final

# def inspect_tokens(tokens):
#     new_tokens=[]
#     for token in tokens:
#         if token in const.keywords:
#             new_tokens.append(token)
#         elif re.match(const.RE_Identifier, token):
#             new_tokens.append(token)
#         elif re.match(const.RE_Literals["text"], token):
#             new_tokens.append(token)
#         elif token.isdigit():
#             new_tokens.append(token)
#         elif token in const.op:
#             new_tokens.append(token)
#         elif token in const.symbols:
#             new_tokens.append(token)
#         else:
#             res=resplit(token)
#             new_tokens += inspect_tokens(res)
#     return new_tokens


# from lexerpy.py

#def tokenize(code):
    # #Tokenizes each line of code from the input file
    # prepcode=prep.prepare(code)
    # tokens=[]
    # for i in range(len(prepcode)):
    #     # if prep.check_token_consistency(prepcode[i]):
    #     #     t=prep.splitmore(prepcode[i])
    #     #     print(t)
    #     #     tokens.append(tk.Token(value=t.value, quality=t.quality))
    #         tokens.append(tk.Token(value=prepcode[i], quality=prep.check_token_consistency(prepcode[i])))
        
    # return tokens
    # for i in code:
    #     pass


and Token[-1] in const.delimiters["n_delim"]

if char 

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


     # print("Error: " + error + " at line " + str(line) + ", position " + str(position) + "."
    # if current is not None:
    #     print(f"Error at {current}")
    #     remaining=re.sub(re.escape(current), '',remaining, count=1)

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

# def is_Lit(Token):
#     if Token in const.boolean:
#         return True
#     else:
#         return False 