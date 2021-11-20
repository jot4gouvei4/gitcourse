#sobreposicao é a capacidade de sobrescrevermos declaracoes de mesmo nome ja declaradas no código
#ex1:

variavel = "valor"
variavel = "valor atualizado"

print("variavel")


#ex2:

variavel = "valor"
variavel = "valor atualizado"

def chamada01():
    print("chamada01")
#metodos fora de classe recebem o nome de funcao qdo nao sao orientados a objetos
def chamada01():
    print("chamada01 atualizada")
def chamada02():
    return "chamada02"
def chamada02():
    return "chamada02 atualizada"

print(variavel)
chamada01()
print(chamada02())


#ex3:

class classe:
    def metodo(self):
        print("metodo 1")

class classe:
    def metodo(self):
        print("metodo 2")

c = classe()
c.metodo()


#ex4:

class classe:
    atributo = "atributo original"
    atributo = "atributo atualizado"

    def __init__(self):
        print ("construçao original")
    def __init__(self):
        print ("construçao atualizada")
    def metodo(self):
        print ("metodo original")
    def metodo(self):
        print ("metodo atualizado")
    def funcao(self):
        return "funcao original"
    def funcao(self):
        return "funcao atualizada"
    def __del__(self):
        print ("destruicao original")
    def __del__(self):
        print ("destruicao atualizada")
    
c = classe()
print(c.atributo)
c.metodo()
print(c.funcao())
del c


#ex5:

class primaria:
    atributo = "atributo pai"

    def __init__(self):
        print("contrucao pai")

    def metodo(self):
        print("metodo pai")

    def funcao(self):
        return "funcao pai"

    def __del__(self):
        print("destruição pai")

class secundaria(primaria):
    atributo = "atributo filha"

    def __init__(self):
        print("contrucao filha")

    def metodo(self):
        print("metodo filha")

    def funcao(self):
        return "funcao filha"

    def __del__(self):
        print("destruição filha")

s = secundaria()
print (s.atributo)
s.metodo()
print(s.funcao())
del s