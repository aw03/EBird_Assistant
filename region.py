class Region:
    def __init__(self, name, code, reg_type, par_name, par_code) -> None:
        self.reg_name = name
        self.reg_code = code
        self.reg_type = reg_type
        self.parent_name = par_name
        self.parent_code = par_code

    def __repr__(self) -> str:
        return self.reg_code
    
    def __str__(self) -> str:
        return self.reg_name
    
    def get_reg_type(self):
        return self.reg_type

    def get_parent_name(self):
        return self.parent_name
    
    def get_parent_code(self):
        return self.get_parent_code
    