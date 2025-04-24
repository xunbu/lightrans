class Recorder():
    maxrecord=50


    def __init__(self):
        self.record=[]
        self.cursor=None

    def addrecord(self,info:str):
        self.record.append(info)
        while len(self.record)>10:
            self.record.pop(0)
        self.cursor=len(self.record)-1

    def clearrecord(self):
        self.record=[]

    def nextrecord(self):
        print('crnext=', self.cursor)
        if self.cursor==None:
            if self.record!=[]:
                return self.record[0]
            else:
                return ''
        if self.cursor==len(self.record)-1:
            return self.record[-1]
        else:
            self.cursor+=1
            return self.record[self.cursor]

    def prerecord(self):
        print('crpre=',self.cursor)
        if self.cursor==None:
            if self.record!=[]:
                return self.record[0]
            else:
                return ''
        if self.cursor==0:
            return self.record[0]
        else:
            self.cursor-= 1
            return self.record[self.cursor]
