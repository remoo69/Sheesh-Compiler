import constants as const
import prepare as prep
import lexerpy as lex
import tokenclass as tkc 

class Error:
    errcount=0
    def __init__(self, errorval=None, remaining=None, line=0, type=None):
        self.errorval = errorval
        self.line=line
        self.remaining=remaining
        self.error_type=type

    def __str__(self) -> str:
        return f"{self.error_type}"

class LexError:

    @staticmethod
    def get_error_symbol(tokencode):
        #error types: invalid delim for symbol, invalid symbol, invalid compound symbol
        buffer = ''
        i = 0
        errobj=Error()
         #invalid delim error
        buffer += tokencode[i]
        if buffer in const.all_op or buffer in const.all_symbols_nonop:
            if i + 1 < len(tokencode):
                if buffer + tokencode[i + 1] in const.all_op:
                    buffer += tokencode[i + 1]
                    if i + 2 < len(tokencode) and buffer + tokencode[i + 2] in const.all_op:
                        buffer += tokencode[i + 2]
                        if i + 3 < len(tokencode) and buffer + tokencode[i + 3] not in const.all_op:
                            errobj.errorval=buffer
                            errobj.remaining=tokencode.replace(buffer, '', 1)
                            errobj.error_type=f"Invalid Delimiter for Symbol '{buffer}', '{tokencode[i + 3]}' "
                            return errobj
                    else:
                        errobj.errorval=buffer
                        errobj.remaining=tokencode.replace(buffer, '', 1)
                        errobj.error_type=f"Invalid Delimiter for Symbol '{buffer}', '{tokencode[i + 2]}' "
                        return errobj
                else:
                    errobj.errorval=buffer
                    errobj.remaining=tokencode.replace(buffer, '', 1)
                    errobj.error_type=f"Invalid Delimiter for Symbol '{buffer}', '{tokencode[i + 1]}' "
                    return errobj
            else:
                errobj.errorval=buffer
                errobj.remaining=tokencode.replace(buffer, '', 1)
                errobj.error_type=f"Invalid Null Delimiter for Symbol '{buffer}' "
                return errobj
        # i += 1

    
    @staticmethod
    def get_error_identifier(tokencode):
        #error types: invalid delim, size too long, invalid char as delim, 
        buffer=''
        i=0
        errobj=Error()
        while i<len(tokencode): #invalid delim error
            if tokencode[i] not in const.delimiters["id_delim"]: 
                buffer+=tokencode[i]
                if len(buffer)>const.MAX_IDEN_LENGTH: #size too long
                    errobj.errorval=buffer
                    errobj.remaining=tokencode.replace(buffer, '', 1)
                    errobj.error_type=f"Invalid Identifier Length. Only '{buffer}' is considered an Identifier"
                    return errobj
                elif len(buffer)==len(tokencode):
                    errobj.errorval=buffer
                    errobj.remaining=tokencode.replace(buffer, '', 1)
                    errobj.error_type=f"Invalid Null Delimiter for Identifier '{buffer}'"
                    return errobj
                if tokencode[i] not in const.invalid_id_char:
                    if not tokencode[0].isalpha(): #invalid first char
                        errobj.errorval=buffer
                        errobj.remaining=tokencode.replace(buffer, '', 1)
                        errobj.error_type=f"Invalid First Character for Identifier"
                        return errobj
                    #delim as invalid char; invalid delim
                    
                    i+=1
                else: 
                    break
            else: return None
        if len(buffer)==len(tokencode):
            errobj.errorval=buffer
            errobj.remaining=tokencode.replace(buffer, '', 1)
            errobj.error_type=f"Invalid Null Delimiter for Identifier '{buffer}'"
        # return buffer, tokencode.replace(buffer, '', 1)

    @staticmethod
    def get_error_numeric(tokencode):
        #error types for numeric: invalid delimiter, invalid size, invalid format for negative
        buffer=''
        i=0
        errobj=Error()
        while i < len(tokencode):
            if tkc.LexerCheck.is_Numeric(buffer) and len(buffer) < len(tokencode):
                if tokencode[i].isdigit():
                    buffer+=tokencode[i]
                    i+=1
                try:
                    if tokencode[i] not in const.delimiters["n_delim"]:
                        # invalid delim
                        errobj.errorval=buffer
                        errobj.remaining=tokencode.replace(buffer, '', 1)
                        errobj.error_type=f"Invalid Delimiter for Numeric '{buffer}', '{tokencode[i]}' "
                        return errobj
                except IndexError:
                    errobj.errorval=buffer
                    errobj.remaining=tokencode.replace(buffer, '', 1)
                    errobj.error_type=f"Invalid Null Delimiter for Numeric '{buffer}' "
                    return errobj
            elif buffer.startswith("-"):
                # invalid format for negative
                errobj.errorval=buffer
                errobj.remaining=tokencode.replace(buffer, '', 1)
                errobj.error_type=f"Invalid Negative Value Format. Enclose Negatives in ( ), '{buffer}'"
                return errobj
            elif buffer.startswith("(") and buffer.endswith(")"):
                # invalid size
                errobj.errorval=buffer
                errobj.remaining=tokencode.replace(buffer, '', 1)
                errobj.error_type=f"Numeric Literal is too Large, '{buffer}'"
                return errobj
            else:
                buffer += tokencode[i]
                i += 1
        try:
            buffer+=tokencode[i+1]
        except IndexError:
            print("idnex error")
        if tkc.LexerCheck.is_Numeric(buffer):
            errobj.errorval=buffer
            errobj.remaining=tokencode.replace(buffer, '', 1)
            errobj.error_type=f"Invalid Null Delimiter for Numeric, '{buffer}'"
            return errobj
        
    @staticmethod
    def get_error_text(tokencode):
        #error types: no closing quote, invalid escape sequence, invalid delim, illegal character
        buffer=''
        i=0
        errobj=Error()
        while i<len(tokencode):
            if tokencode.startswith('"'):
                buffer += tokencode[i]
                i += 1
                if len(buffer)==len(tokencode):
                    errobj.errorval=buffer
                    errobj.remaining=tokencode.replace(buffer, '', 1)
                    errobj.error_type=f"No Closing Quote for {buffer}"
                    return errobj
            else: return None

                
        # return buffer, tokencode.replace(buffer, '', 1)

    @staticmethod
    def get_errors(tokencode): #this should return the errotype as well
        if tokencode is None:
            return None
        elif LexError.get_error_numeric(tokencode):
            return LexError.get_error_numeric(tokencode)
        elif LexError.get_error_identifier(tokencode):
            return LexError.get_error_identifier(tokencode)
        elif LexError.get_error_symbol(tokencode):
            return LexError.get_error_symbol(tokencode)
        elif LexError.get_error_text(tokencode):
            return LexError.get_error_text(tokencode)
        
    # @staticmethod
    # def error_type(errorval, remaining):
    #     category=tkc.LexerCheck.categorize(errorval)
    #     if category=="Keyword":
    #         return f"Invalid Delimiter for Keyword {errorval}"
    #     elif category=="Identifier":
    #         if len(errorval)>const.MAX_IDEN_LENGTH:
    #             return f"Identifier {errorval} exceeds maximum length of {const.MAX_IDEN_LENGTH}"
    #         elif errorval[0].isdigit():
    #             return f"Invalid first character for Identifier {errorval}"
    #         else:
    #             return f"Invalid Delimiter for Identifier {errorval}"
    #     elif category=="Numeric":
            
# print(LexError.get_error_identifier(test))