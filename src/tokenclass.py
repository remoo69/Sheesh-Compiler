class Token:
    def __init__(self, type=None, value=None, line=None, position=None, attribute=None):
        self.value = value
        self.type = type
        self.attribute=attribute
        self.line = line
        self.position = position
        

