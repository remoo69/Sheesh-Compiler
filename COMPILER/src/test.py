import re
import constants as const
import lexerpy as lex

class NumericLexer:
    def __init__(self):
        # Define regular expressions for integers and floats
        integer_pattern = re.compile(r'\d+')
        float_pattern = re.compile(r'\d+\.\d+')

        # Create the DFA transitions for integers and floats
        self.transitions = {
            'start': {'digit': 'integer', '.': 'float_start'},
            'integer': {'digit': 'integer', '.': 'float_start'},
            'float_start': {'digit': 'float'},
            'float': {'digit': 'float'},
        }

        # Define accepting states
        self.accepting_states = {'integer', 'float'}

        # Map regular expressions to DFA states
        self.regex_to_state = {
            integer_pattern: 'integer',
            float_pattern: 'float',
        }

    def process_input(self, input_string):
        current_state = 'start'
        token = ''
        position = 0

        while position < len(input_string):
            char = input_string[position]

            if char.isdigit():
                input_symbol = 'digit'
            elif char == '.':
                input_symbol = '.'
            else:
                input_symbol = 'other'

            next_state = self.transitions.get(current_state, {}).get(input_symbol, None)

            if next_state:
                current_state = next_state
                token += char
                position += 1
            else:
                break  # Invalid transition, break the loop

        if current_state in self.accepting_states:
            return token, current_state
        else:
            return None, None

    def tokenize(self, input_string):
        tokens = []

        while input_string:
            match = None

            for pattern, state in self.regex_to_state.items():
                match = pattern.match(input_string)

                if match:
                    value = match.group(0)
                    input_string = input_string[len(value):]

                    if state in self.accepting_states:
                        tokens.append((state, value))

                    break

            if not match:
                # If no match is found, there's an invalid token
                print("Invalid token detected.")
                break

        return tokens

# Example usage
# numeric_lexer = NumericLexer()
# input_string = "123 45.67 89. .456"
# tokens = []
# token2=[]

# while input_string:
#     token, final_state = numeric_lexer.process_input(input_string)

#     if token is not None:
#         tokens.append((final_state, token))
#         input_string = input_string[len(token):].lstrip()
#     else:
#         print("Invalid input.")
#         break

# print("Input:", input_string)
# print("Tokens:", tokens)
# print(const.all_op)

# def is_valid_text(input_string):
#     if not input_string.startswith('"') or not input_string.endswith('"'):
#         return False

#     escaped = False
#     for char in input_string[1:-1]:
#         if escaped:
#             escaped = False
#         elif char == '\\':
#             escaped = True
#         elif char == '"':
#             return False

#     return not escaped

# # Example usage
# valid_text = '"This is a valid string with escaped quotes: \\"Inside Quotes\\"."'
# invalid_text = 'This is not a valid text.'

# print(is_valid_text(valid_text), valid_text)    # Output: True
# print(is_valid_text(invalid_text))  # Output: False
# def error_handler(buffer, nextchar, errorlist: list):
#     if buffer is None:
#         errorlist.append("Invalid Token")
#         return errorlist
#     elif lex.is_Valid_Token(buffer) and nextchar not in:
#         errorlist.append(f"Invalid Delimiter for {lex.categorize(buffer)}: {buffer}" )
        return errorlist
def old_get_symbol(token):
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
def get_symbol(token): #changed
    token_cpy = token
    current_state = 'start'
    compound_op_buffer = ''

    for i, char in enumerate(token):
        if char in const.symbols:
            try:
                next_temp = char + token[i + 1]
                next_next_temp = next_temp + token[i + 2]
            except IndexError:
                next_temp = char
                next_next_temp = ''

            if next_next_temp == '...':
                if token[i + 3] not in const.symbols_delims[next_next_temp]:
                    return None
                token_cpy = token.replace(next_next_temp, '', 1)
                return next_next_temp, token_cpy

            if next_temp in const.compound_symbols:
                if token[i + 2] not in const.symbols_delims[next_temp]:
                    return None
                token_cpy = token.replace(next_temp, '', 1)
                return next_temp, token_cpy

            # Handle combined operators like '+=', '-=', etc.
            if char in current_state:
                current_state = const.symbols_delims[char]
                compound_op_buffer += char
            else:
                # If the current character doesn't fit the current state, reset the buffer and state
                compound_op_buffer = ''
                current_state = 'start'

            if current_state == 'final':
                token_cpy = token.replace(compound_op_buffer, '', 1)
                return compound_op_buffer, token_cpy
        else:
            return None
def get_operator(tokencode:str):
    position=0
    token=''
    token_cpy=''
   
    char=tokencode[position]
    if char==".": #isolated case for ...
        token+=char
        if tokencode[position+1]==".":
            token+=tokencode[position+1]
            if tokencode[position+2]==".":
                token+=tokencode[position+2]
                if tokencode[position+3] in const.symbols_delims["..."]:
                    token_cpy=tokencode.replace(token, '', 1)
                    return token, token_cpy
    elif char in const.single_symbols:
        token+=char
        if tokencode[position+1] in const.symbols_delims[char]:
            token_cpy=tokencode.replace(char, '', 1)
            return char, token_cpy
        else: #else, it should be compound
            position+=1
            token+=tokencode[position]    
            if token not in const.compound_symbols:
                return None
                # token_cpy=tokencode.replace(token, '', 1)
                # return f"Invalid Delimiter {tokencode[position]}", token_cpy    
            else:
                position+=1
                token_cpy=tokencode.replace(token, '', 1)
                if tokencode[position] in const.symbols_delims[token]: #if valid delim for compound symbol  
                    return token, token_cpy
                else:
                    return None
def getsymbol(token):
    for i, char in enumerate(token):
        if char in const.grouping_symbols and token[i+1] in const.symbols_delims[char]:
            return char, token.replace(char, '', 1)
        else:
            if char in const.other_symbols: 
                return char, token.replace(char, '', 1)
            elif token[i:i+2] in const.other_symbols:
                return token[i:i+2], token.replace(token[i:i+2], '', 1)

def get_block_comments(input_code):
    output_code = ""
    in_block_comment = False

    i = 0
    while i < len(input_code):
        if input_code[i:i+2] == '/*' and not in_block_comment:
            in_block_comment = True
            i += 2
            output_code+="/*"
        elif input_code[i:i+2] == '*/' and in_block_comment:
            in_block_comment = False
            i += 2
            output_code+="*/"
            break
        else:
            output_code+=input_code[i]
            i += 1
    input_code=input_code.replace(output_code, '', 1)
    return output_code, input_code

def new_tokenize(code):
    for char in code:
        pass


