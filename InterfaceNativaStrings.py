# interface padrão __str__ 


#Ex. 1:

class Texto:
    def __str__(self):
        return "texto"

t = Texto()
print(t.__str__())


#Ex. 2:

class Texto:
    def __str__(self):
        return "texto"

t = Texto()
print(t)
#Sempre deve retornar string


#Ex. 3:

class Texto:
    def __str__(self):
        return "5"

t = Texto()
print(t)
#Para retornar um número ele deve ser escrito como string


#Ex. 4:

class Texto:
    atributo = "atributo"
    def __str__(self):
        return "texto"
    def metodo(self):
        print("metodo")
    def funcao(self):
        return "funcao"


t = Texto()
print(t)
print(t.atributo)
t.metodo()
print(t.funcao())
