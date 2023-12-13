import lexerpy as lex
import prepare as prep
import constants as const
import re
import time
import pandas as pd
from tabulate import tabulate
import error_handler as err
import tokenclass as tkc

# test="use somewhere#"
# print(prep.gettokens(test))
# print(lex.tokenize(test))
# print(test[0].isalpha())
# print(prep.remove_comments(prep.file_to_string(r"input1.sheesh")))

# tokens, error=lex.Lexer.tokenize(prep.file_to_string(r"input1.sheesh"))
# tokenlist=[]
# categorylist=[]
# errorlist=[]
# errcat=[]
# for i in range(len(tokens)):
#     tokenlist.append(tokens[i].value)
#     categorylist.append(tokens[i].type)

# for j in range(len(error)):
#     errorlist.append(error[j].errorval)
#     errcat.append(error[j].error_type)

# # tokens, category = prep.remove_whitespace_type(tokens, category)
# df=pd.DataFrame({'Token':tokenlist, 'Type':categorylist})
# print(tabulate(df.values.tolist(), headers=df.columns.tolist(), tablefmt='psql'))
# print(errorlist, errcat)

test="20"
# print(len(test))
# print(lex.Lexer.gettokens(test))

print(err.LexError.get_error_numeric(test))
# print(prep.get_whole(test))
# print(tkc.LexerCheck.is_Whole(test))

# print(tkc.LexerCheck.is_Numeric("-9999999"))
# print(err.LexError.get_errors(test))
# print(prep.get_symbol(test))
# print(lex.Lexer.gettokens(test))
#getspace prblem
# test="=#5"
# print("Input is:", test)
# tokens,errors=lex.Lexer.gettokens(test)
# print("tokens:\n")
# for token in tokens:
#     print(f"[Value: {token.value}, Type: {token.type}]")

# print("\n\nerrors:\n")
# for error in errors:
#     print(error.errorval)

# print(err.LexError.get_error_symbol(test))

# test="dec abc= 5#"

# print(lex.Lexer.tokenize(test))
# # # print(tkc.LexerCheck.is_Text(test))
# print(err.LexError.get_error_text(test))
# # test="....\""
# # print(lex.Lexer.gettokens(test))
# print(err.LexError.get_error_symbol(test))
# print(bool("=" in const.invalid_id_char))
# print(err.LexError.get_errors(test))

# # print(const.symbols_delims["::"])
# def add(a, b):
#     return a+b

# print(add(8**2, 1))
# class test:
#     def __init__(self, value, index) -> None:
#         self.value=value
#         self.index=index

# testlist=[]
# for i in range(4):
#     testobj=test(5, 6+i)
#     testlist.append(testobj)

# for n in range(4):
#     print(testlist[n].value, testlist[n].index)
# print(lex.Lexer.is_Identifier(test))
# print(lex.Lexer.is_Identifier(test2))
# print(lex.Lexer.is_Identifier(test3))
# # print(test[2])
# print(test[0:2])

# result=prep.get_symbol(token)
# print(result)
# if result:
#     print(result)
# else:
#     print("Invalid delimiter")
#     print(prep.get_error_symbol(test))
# if result:
#     print(result)
# else:
#     prep.get_error(test)
# test="//this is a sample inline comment whole sheesh smh"
# print(prep.get_inline_comments(test))

# print(prep.gettokens(test))
# print("Tested: ", test)
# print(lex.is_Valid_Token(""))
# test="=5#"
# print(prep.get_symbol(test))

# test="use something from somewhere#"
# print(prep.get_keyword(test))

# token='"hel\\"los"'
# print(lex.is_Text(token), token)
# # def gettokens(code):
#     # Iterate through a line of code per character and return as a list of tokens
#     # Check each character
#     tokencode = code
#     tokens = []
#     current_token:str = ''
#     tktype = ''

#     while tokencode:
#         if get_keyword(tokencode):
#             result=get_keyword(tokencode)
#             if result is not None:
#                 current_token, tokencode = result
#             else: continue
#             tktype = "keyword"
#         elif get_identifier(tokencode):
#             result=get_identifier(tokencode)
#             if result is not None:
#                 current_token, tokencode = result
                
#             else: continue
#             tktype = "identifier"
#         elif get_text(tokencode):
#             result=get_text(tokencode)
#             if result is not None:
#                 current_token, tokencode = result
#             else: continue
#             tktype = "text"
#         elif get_dec(tokencode):
#             result=get_dec(tokencode)
#             if result is not None:
#                 current_token, tokencode = result
#             else: continue
#             tktype = "dec"
#         elif get_whole(tokencode):
#             result=get_whole(tokencode)
#             if result is not None:
#                 current_token, tokencode = result
#             else: continue
#             tktype = "whole"
#         elif get_symbol(tokencode):
#             result=get_symbol(tokencode)
#             if result is not None:
#                 current_token, tokencode = result
#             else: continue
#             tktype = "symbol"
#         else:      #problem
#             if tokencode:
#                 if current_token is None or current_token=='':
#                     current_token=tokencode
#                     tokens.append(tokencode)
#                     tokencode=None
#                     tokens.append(None)
#                     break
#             else:
#                 tokens.append("None")
#                 break
            
        
#         if current_token:
#                 tokens.append(current_token)
#                 current_token = ''
#         else: #Handles null chars
#             print("Else labas gettokens")
#             error=lex.error_handler(None, tokens, None)
#             print(error, "for", current_token)
#     return tokens


# print(prep.remove_comments(prep.file_to_string(r"input1.sheesh")))
# space=" "
# test=" hello there"
# print(test.replace(" ", '', 1))
# print(test, prep.get_space(test))
# token="(-1.5)"
# space=" "
# test.replace(space, "")
# print(test)
# print(token.startswith("(") and token.endswith(")"))


# print(lex.is_Valid_Token("_letter"))
# remain=["=", "45", "="]
# teststring="whole#"
# test2="yessir"
# print(lex.categorize(teststring))
# print(lex.categorize(test2))
# test=["hello", " ", "error"]
# print(lex.error_handler(test2 ,remain, test ))
# print(bool(lex.is_Literal(test2)))
# print(bool(test2 in const.delimiters["op"]))
# print(bool(lex.is_Literal(test2)))
# if test2 not in const.delimiters["op"] and not lex.is_Literal(test2) and not lex.is_Identifier(test2):
#     print( "yeppssir")

# else:
#     print("else")
# remaining=['#']
# test="idtnidentifiere"
# print(bool(re.match(const.RE_Identifier, test)))
# print(lex.error_handler(test, prev, test))
# listnew=["1", "2"]
# listnew.append(None)
# print(listnew)

# test=["hello", " ", "error"]
# error=lex.error_handler(None, test, None)
# print(error)
# print(error)

# tokens=['"hello"']
# remaining="this is a test"
# error="..."
# test="iden$fsd"
# print(lex.categorize(test))
# print(lex.error_handler(test, tokens, remaining=remaining))
# code = prep.file_to_string(r"input1.sheesh")
# tokens = prep.prepare(code)
# # print(code)
# time.sleep(1)
# print(tokens)
# time.sleep(1)
# print(bool(lex.is_Identifier("EOF")))
# print(tokens)
# print(tokens, "\n")
# fintokens=[]
# category=[]
# table={}
# for line in tokens:
#     lines=prep.gettokens(line)
#     for token in lines:
#         fintokens.append(token)
#         category.append(lex.categorize(token))

# df=pd.DataFrame({'Token':fintokens, 'Type':category})
# print(tabulate(df.values.tolist(), headers=df.columns.tolist(), tablefmt='psql'))

# print(repr("hello\nhello"))
# test="=="
# test2="="
# test3="==="
# test4="-="
# test5="..."
# test6="|"
# tests=[test, test2, test3, test4, test5, test6]

# for i in tests:
#     print(i)
#     print(bool(lex.is_Operator(i)))
#     print(bool(lex.is_Symbol(i)))
    
# print(lex.categorize(r'"whole \"hellowhole"'))

    # for i in tokens:
    #     fintokens.append(i)
    #     print(f"\n\nLine:{line}\nToken: {i}\nType: {lex.categorize(i)}")
    # print(f"Token: {prep.gettokens(line)}\nType: {lex.categorize(prep.gettokens(line))}")
# for i in range(len(fintokens)):
#     for j in range(len(fintokens[i])):
#         table.update({fintokens[i][j]: lex.categorize(fintokens[i][j])})
# df=pd.DataFrame(table.items(), columns=['Token', 'Type'])
# print(tabulate(df.values.tolist(), headers=df.columns.tolist(), tablefmt='psql'))


# li=['n', '-=']
# test='n-=bgdfg'

# # print(lex.error_handler(test, li))
# print(prep.gettokens(test))

# print(lex.categorize("20 "))


# test="........"
# print(bool(lex.is_Symbol(test)))
# print(bool(test in const.symbols))
# print(bool(test in const.concat))


# prev=['i', 'j', '...']
# error=lex.error_handler('"hello"',prev)
#for ... " works as delim but "text" isn't considered


# string="gg pare"
# tok=prep.gettokens(string)
# print(tok)

# # {bigay(\"Hello\"...\"ito\")#}
# result = prep.gettokens("{bigay(\"Hello\"...\"ito\")#}") 
# print(result)

# text=prep.get_text("\"Hello\"...\"ito\"")
# if text is not None:
#     lex,trash=text
#     print(lex)
#     print(trash)
# symb=prep.get_symbol(trash)
# lex,trash=symb
# print(lex)
# print(trash)



# # # tokens=prep.get_whole("5)")
# tokens=prep.gettokens("(i==5)")
# tokens=prep.gettokens("i+=5#")
# print(tokens)
# space=prep.get_space(" i+=5#")
# print(space)
# sym, left=prep.get_space(" ==5#")
# print(sym, left)
# print(lex.is_Dec("1234."))
# print(lex.is_Dec("1234"))
# print(lex.is_Dec("-1234"))
# print(lex.is_Dec("-1234."))
# print(lex.is_Dec("1234.1234"))#true
# print(lex.is_Dec("-1234.1234")) 
# print(lex.is_Dec("(-1234.1234)"))#true
# print(lex.is_Dec("(-1234.1234)/"))#true w/delim
# print(lex.is_Dec("(-1234.1234)*"))
# print(lex.is_Dec("0.0000"))
# print(lex.is_Dec("0.0000+"))
# print(lex.is_Dec("-0"))
# print(lex.is_Dec("-0.0000"))
# print(lex.is_Dec("(-0.0000)"))

# sample_values = [
#     "0",
#     "1",
#     "12",
#     "123",
#     "1234",
#     "(-0)",
#     "(-1)",
#     "(-12)",
#     "(-123)",
#     "(-1234)",
#     "(-0.0)",
#     "(-1.0)",
#     "(-12.0)",
#     "(-123.0)",
#     "0.0",
#     "1.0",
#     "12.0",
#     "123.0",
#     "0.000000",
#     "0000.0000",
#     "0.1234",
#     "1234.1234"
# ]
# for i in sample_values:
#     print(i, bool(re.match(const.RE_Literals["pos_dec"], i) or re.match(const.RE_Literals["neg_dec"], i)))


# for i in range(len(tokens)):
#     for pos in range(len(tokens[i])):
#         print(lex.is_Text(tokens[i][pos]))
# text="\"hello\"#"
# whole="1234+"
# whole2="0="
# whole3="(-1234)/"
# whole4="(-1205)*"
# whole5="6]"
# print(lex.is_Whole(whole))
# print(lex.is_Whole(whole2))
# print(lex.is_Whole(whole3))
# print(lex.is_Whole(whole4))
# print(lex.is_Whole(whole5)) 
# test="=+"
# tokens, errors=lex.Lexer.gettokens(test)

# for i in range(len(tokens)):
#     print(tokens[i].value)
#     print(errors[i].errorval)