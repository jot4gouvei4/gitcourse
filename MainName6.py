#modo1 - quando não formos usar tds as classes, para não sobrecarregar o processamento sem necessidade

from MainName5 import Classe1, Classe3

c1 = Classe1()
c3 = Classe3()

c1.metodo1()
c3.metodo3()

#modo2 - * = tds as Classes

from MainName5 import *

c1 = Classe1()
c2 = Classe2()
c3 = Classe3()

c1.metodo1()
c2.metodo2()
c3.metodo3()