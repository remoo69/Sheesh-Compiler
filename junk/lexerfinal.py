import tokenizer 

class Lexer:
    class Token:
        def __init__(self, type, value=None, line=None, position=None):
            self.type = type
            self.value = value
            self.line = line
            self.position = position
