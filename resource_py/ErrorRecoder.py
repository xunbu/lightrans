class ErrorRecoder():
    def __init__(self):
        self.error=[]

    def adderror(self,error:str)->None:
        self.error.append(error)

    def print_error_clear(self)->str:
        result='\n'.join(self.error)
        self.error.clear()
        return result

errorrecoder=ErrorRecoder()