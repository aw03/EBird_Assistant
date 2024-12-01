class Region:
    def __init__(self, name, code, parent) -> None:
        self.reg_name = name
        self.reg_code = code
        self.parent = parent

    def __repr__(self) -> str:
        return self.reg_code
    
    def __str__(self) -> str:
        return self.reg_name

    def get_parent(self):
        return self.parent
    