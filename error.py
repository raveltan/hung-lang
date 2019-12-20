class Error:
    def __init__(self,position_start,position_end,error_name,details):
        self.error_name = error_name
        self.position_start = position_start
        self.position_end = position_end
        self.details = details
    def __str__(self):
        return f'\n{self.position_start.file_name}:{self.position_start.line_number}:{self.position_start.index}:\
 ERROR: {self.error_name} {self.details}\n'

class IllegalCharacterError(Error):
    def __init__(self,position_start,position_end,details):
        super().__init__(position_start,position_end,'Illegal Character',details)
