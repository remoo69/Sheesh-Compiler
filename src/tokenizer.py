import prepare as prep
import constants as const
import error_handler as err

class Lexer:
    @staticmethod
    def gettokens(code):
    # Iterate through a line of code per character and return as a list of tokens
    # Check each character
        tokencode = code
        tokens = []
        errors=[]
        current_token:str = ''
        tktype = ''

        while tokencode:
            if prep.get_keyword(tokencode):
                result=prep.get_keyword(tokencode)
                if result:
                    current_token, tokencode = result
                else: continue
                tktype = "keyword"
            elif prep.get_identifier(tokencode):
                result=prep.get_identifier(tokencode)
                if result:
                    current_token, tokencode = result
                else: continue
                tktype = "identifier"
            elif prep.get_inline_comments(tokencode):
                result=prep.get_inline_comments(tokencode)
                if result:
                    current_token, tokencode = result
                else: continue
            elif prep.get_text(tokencode):
                result=prep.get_text(tokencode)
                if result:
                    current_token, tokencode = result
                else: continue
                tktype = "text"
            elif prep.get_dec(tokencode):
                result=prep.get_dec(tokencode)
                if result:
                    current_token, tokencode = result
                else: continue
                tktype = "dec"
            elif prep.get_whole(tokencode):
                result=prep.get_whole(tokencode)
                if result:
                    current_token, tokencode = result
                else: continue
                tktype = "whole"
            elif prep.get_symbol(tokencode):
                result=prep.get_symbol(tokencode)
                if result:
                    current_token, tokencode = result
                else: continue
                tktype = "symbol"
            elif prep.get_operator(tokencode):
                result=prep.get_operator(tokencode)
                if result:
                    current_token, tokencode = result
                else: continue
            elif prep.get_space(tokencode):
                result=prep.get_space(tokencode)
                if result:
                    current_token, tokencode = result
                else: continue
            else:
                result = err.LexError.get_errors(tokencode)
                if result:
                    errorval, tokencode = result
                    errors.append(errorval)
                    
            #     if tokencode:
            #         if current_token is None or current_token=='':
            #             # print("interrif")
            #             # current_token=tokencode
            #             # tokens.append(tokencode)
            #             # tokencode=None
            #             # tokens.append(None)
            #             break
                
            #     else:
            #         # result=err.LexError.error_handler(tokencode, None, None)
            #         pass
            
            if current_token:
                    # token_obj=tk.Token(value=current_token, type=tktype)
                    tokens.append(current_token)
                    current_token = ''
            else: #Handles null chars
                # print("May error par", current_token, tokencode)
                # error=err.LexError.error_handler(None, tokens, None)
                # print(error, "for", current_token)
                pass
        return tokens, errors
    
    @staticmethod    
    def tokenize(codes):
        lines = prep.prepare(codes)
        tokens=[]
        category=[]
        error=[]
        for i,line in enumerate(lines):
            lexeme, errors=Lexer.gettokens(line)
            for j,token in enumerate(lexeme):
                if token is None or LexerCheck.categorize(token) not in const.valid_tokens:
                    print(token,"errcat")
                    # errortype=Lexer.error_handler(token, tokens, lexeme[j+1:])
                    # error.append(f"Line {i+1}: {errortype}")
                else:
                    tokens.append(token)
                    category.append(LexerCheck.categorize(token))
                
                # elif 

                
        
        # error=error_handler
        return tokens, category, error
    # @staticmethod    
    # def error_handler(current, tokenized, remaining):
    #     print(f"pumasok ay {current, tokenized, remaining}")
    #     error_val = current
    #     try:
                        
    #         if current=='' or current is None:
    #             return f"Type 1 Invalid Null Delimiter for \"{tokenized[-1]}\", remaining: {remaining}"
    #         # This portion is for delimiter mismatches
    #         if remaining is None and not Lexer.is_Symbol(error_val):
    #             return f"Type 2 Invalid Null Delimiter for \"{current}\""
            
    #         if not Lexer.is_Valid_Token(current):
    #             return f"{current} is not a valid Token"

    #         if Lexer.categorize(error_val) == "Error Category":
    #                 return f"{error_val} Invalid Syntax for Token"

    #         if Lexer.is_Identifier(error_val) and len(error_val)>9:
    #             return f"Type 3 Identifier {error_val} contains legal characters but is too long "
    #         # Categorize previously matched token
    #         token_prev = tokenized[-1]
    #         category = Lexer.categorize(token_prev)

    #         # Check if the delimiter is valid for the token category (prev)
    #         if category == "Keyword":
    #             if error_val not in const.keywords_delims[tokenized[-1]]:
    #                 return f"Invalid Delimiter for \"{category}\", \"{token_prev}\""
    #         elif category == "Identifier":
    #             if error_val not in const.delimiters["id_delim"]:
    #                 return f"Invalid Delimiter for \"{category}\", \"{token_prev}\""
    #         elif category == "Symbol":
    #             if not Lexer.is_Numeric(error_val) and not Lexer.is_Identifier(error_val) and not Lexer.is_Operator(error_val):
    #                 return f"{error_val} Invalid Delimiter for \"{category}\", \"{token_prev}\""
    #         elif category == "Operator":
    #             if error_val not in const.delimiters["op"] and not Lexer.is_Literal(error_val) and not Lexer.is_Identifier(error_val):
    #                 return f"Invalid Delimiter for \"{category}\", \"{token_prev}\""
    #         elif category == "Text":
    #             if error_val not in const.delimiters["txt_delim"] and error_val not in const.concat:
    #                 return f"Invalid Delimiter for \"{category}\", \"{token_prev}\""
    #         elif category in ["Whole", "Dec"]:
    #             if error_val not in const.delimiters["n_delim"] :
    #                 return f"Invalid Delimiter for \"{category}\", \"{token_prev}\""
    #         elif category=="Whitespace":
    #             if error_val not in const.delimiters["space_delim"] or Lexer.categorize(error_val) not in const.valid_tokens:
    #                 return f"Invalid Delimiter for \"{category}\", \"{token_prev}\""

            
    #         else: #if not delim error, then could be token syntax error. 
    #             return "Invalid Token Syntax"
            
    #     except IndexError:
    #         return "Invalid Delimiter and Statement"




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
