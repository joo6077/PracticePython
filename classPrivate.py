class Cal(object):
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v1, int):
            self.v2 = v2
        
        print(v1,v2)
    def add(self): 
        return self.v1+self.v2
    def subtract(self):
        return self.v1-self.v2
    #private 같은
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
    def getV1(self):
        return self.v1
    def getV2(self):
        return self.v2 

c1 = Cal(10,10)
print(c1.add()) 
print(c1.subtract())

