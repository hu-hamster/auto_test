
class BaseCmd():
    
    def __init__(self, expression, desc, until, *args) -> None:
        self.expression = expression
        self.desc = desc
        self.until = until
        
    