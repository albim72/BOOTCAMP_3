class Test:
    def __init__(self,a):
        self.a=a

class T1:
    pass


class Regular(Test,T1):
    pass

reg = Regular(34)
print(reg.a)

#metaklasa ograniczająca wielodziedziczenie

class MultiBases(type):
    def __new__(cls,clsname,bases,attribs):
        if len(bases) > 1:
            raise  TypeError("Wielodziedziczenie jest zabronione!")
        return super().__new__(cls,clsname,bases,attribs)

class Base(metaclass=MultiBases):
    pass

class Extra:
    pass

class A(Base):
    pass

class C(A,Extra):
    pass
