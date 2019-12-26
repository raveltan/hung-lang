class Error:
    def __init__(self,name,file_name,desc,cursor,line,text:str):
        self.name=name
        self.desc = desc
        self.file_name = file_name
        self.cursor = cursor
        self.line = line
        self.text:str = text
    def __repr__(self):
        error = f'\n<{self.file_name}:{self.line}:{self.cursor}> {self.name}, {self.desc}'
        detail = f'\n{self.text}\n' +' '* self.cursor + '^'
        return str(error+detail)
class IllegalSyntax(Error):
    def __init__(self,file_name,desc,cursor,line,text):
        super().__init__('Illegal Syntax',file_name,desc,cursor,line,text)

class UnknownSyntax(Error):
    def __init__(self,file_name,desc,cursor,line,text):
        super().__init__('Unknown Syntax',file_name,desc,cursor,line,text)

class RuntimeError(Error):
    def __init__(self,file_name,desc,cursor,line,text):
        super().__init__('Runtime Error',file_name,desc,cursor,line,text)