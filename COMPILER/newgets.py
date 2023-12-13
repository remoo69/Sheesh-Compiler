'''
pseudocode:

tokenize(Tokenlist):
    for char in tokenlist:
    if char is valid startstate:
        if char is valid nexstate based on startstate:
            buffer+=char
            state=activestate
            if char is valid delimiter (finalstate):
                state=finalstate
            else: invalid delim

                if buffer is valid token:
                    add token as object to tokens
                    val=val
                    state=finalstate
                    buffer=''
                else:
                    add buffer to error_buffer
                    state=errorstate
                    buffer=''

new
    for char in code:
        if state=start #assumes that buffer is none
            add char to buffer
        else
            append char to buffer
            
            
'''

import lexerpy as lex
import prepare as prep
# import tokenclass as tkc
import constants as const

# def tokenize(Tokenlist):
#     code=Tokenlist
#     buffer=tkc.Token()
#     error_buffer=''
#     tokens=[] #stores a list of objects
#     errors=[] #idk if this is needed since I implimented the status in the object           
#     for i in code:
#         if buffer.state=="Start": 
#             #preprod: define all possible start states
#             if i in const.StartStates:

#             buffer.value=i
#             buffer.state="Active"
#         if buffer.state=="Active":
#             #preprod: define all possible next states
#             buffer.value+=i
#         if buffer.state=="End":
#             #preprod: delims already defined; implement
#             buffer.state="End"

#TD

td={#startstate, activestate, finalstate, errorstate
    # "+":{"Final":const.delimiters["delim5"], "Active":{"=":const.delimiters["delim5"]}},
    "+":{"=":"Active", const.delimiters["delim5"]:"Final"},
    ".":{"Active":{".":{
                        "Active":
                                {"Active": ".", "Final": const.delimiters["delim20"]}
                                }
                                }
                                },
}

def newgetsymbol(inputval):
    buffer=''
    if len(inputval)>1:
        for i, char in enumerate(inputval):
            if char in td:
                buffer+=char
                if inputval[i+1] in td[char]["Active"]:
                    buffer+=inputval[i+1]
                    if inputval[i+2] in td[char]["Final"]:
                        buffer+=inputval[i+2]
                        inputval=inputval[i+1:]
                        return buffer, inputval
                    else:
                        if inputval[i+2] in td[char]["Active"]["Active"]:
                            buffer+=inputval[i+2]
                            if inputval[i+3] in td[char]["Active"]["Active"]["Final"]:
                                buffer+=inputval[i+3]
                                inputval=inputval[i+2:]
                                return buffer, inputval
                            else:
                                inputval=inputval[i+2:] 
                                return "Invalid Delimiter", inputval
                    
                elif inputval[i+1] in td[char]["Final"]:
                    inputval=inputval[i:]
                    return buffer, inputval
                
                else: return "Invalid Symbol", inputval
    else:
        return "Invalid Size"
    

print(bool("." in td["."]["Active"]["Active"]))