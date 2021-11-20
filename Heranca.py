#Herança é a capacidade de uma classe em herdar caracteristicas de outra classe
# class x(y): onde x é a primária e y a secundaria
# usa-se o self para chamar um metodo ou funcao existentes(ex: self.metodo/self.funcao)

class classe1:
    atributo1 = "atributo classe1"

    def metodo1(self):
        print("metodo classe1")

    def funcao1(self):
        return "função classe1"


class classe2(classe1):
    atributo2 = "atributo classe2"

    def metodo2(self):
        print("metodo classe2")

    def funcao2(self):
        return "função classe2"

c2 = classe2()
print(c2.atributo1)
print(c2.atributo2)
c2.metodo1()
c2.metodo2()
print(c2.funcao1())
print(c2.funcao2())


#exemplo 2

class pai:
    atributo = "atributo classe pai"
    def metodo(self):
        print("metodo da classe pai")

    def funcao(self):
        return "função da classe pai"

class filha:
    atributo = "atributo classe filha"
    def metodo(self):
        print("metodo da classe filha")

    def funcao(self):
        return "função da classe filha"

f = filha()
print(f.atributo)
f.metodo()
print(f.funcao())


#exemplo 3

class classe1:
    def metodo1(self):
        print("metodo1")

class classe2(classe1):
    def metodo2(self):
        print("metodo2")

class classe3(classe2):
    def metodo3(self):
        print("metodo3")

class classe4(classe3):
    def metodo4(self):
        print("metodo4")

c4 = classe4()
c4.metodo1()
c4.metodo2()
c4.metodo3()
c4.metodo4()