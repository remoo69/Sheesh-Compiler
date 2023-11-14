import lexerpy as lex
import prepare as prep
import constants as const
import re
import time
import pandas as pd
from tabulate import tabulate


# test="=#"
# print(lex.tokenize(test))
# tokens, category, error=lex.tokenize(prep.file_to_string(r"input1.sheesh"))
# tokens, category = prep.remove_whitespace_type(tokens, category)
# df=pd.DataFrame({'Token':tokens, 'Type':category})
# print(tabulate(df.values.tolist(), headers=df.columns.tolist(), tablefmt='psql'))

# print(error)

print(lex.is_Text("\"hello there\""))

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
