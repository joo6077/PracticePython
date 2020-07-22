class C:
    def __init__(self, v):
        #__ pritvate
        self.__value = v
    def show(self):
        print(self.__value)
    

c1 = C(10)
c1.show()