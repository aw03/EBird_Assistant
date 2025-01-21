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
    

class Hotspot:
    def __init__(self, name, code) -> None:
        self.hot_name = name
        self.loc_id = code

    def __repr__(self) -> str:
        return self.loc_id
    
    def __str__(self) -> str:
        return self.hot_name