class Szemely:
    def __init__(self, nev, kor):
        self.nev = nev
        self.kor = kor

szemely1 = Szemely("Mark", 30)
print ("Hello " + szemely1.nev, szemely1.kor)
       
#szelekcio
def ParosE(szam):
    if szam%2==0:
        print("A szam paros")
    else:
        print("A szam paratlan.")
print(ParosE(3))