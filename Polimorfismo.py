#Polimorfismo é a possibilidade de escolher o recurso de mesmo nome entrre classes diferentes que iremos usar

class base:
    atributo = "atributo base"

    def __init__(self):
        print("construtor da base")

    def metodo(self):
        print("metodo base")

    def funcao(self):
        return "funcao base"

    def __del__(self):
        print("destrutor base")

class derivada(base):
    atributo = "atributo derivada"

    def __init__(self):
        print("construtor da derivada")

    def metodo(self):
        print("metodo derivada")

    def funcao(self):
        return "funcao derivada"

    def __del__(self):
        print("destrutor derivada")

d = derivada()
print(d.atributo)
d.metodo()
print(d.funcao())
del d

#usando SUPER() - exceto fora de metodos:
#usando SELF. para chamar recurso da classe que estamos programando

class base:
    atributo = "atributo base"

    def __init__(self):
        print("construtor da base")

    def metodo(self):
        print("metodo base")

    def funcao(self):
        return "funcao base"

    def __del__(self):
        print("destrutor base")

class derivada(base):
    atributo = base.atributo

    def __init__(self):
        super().__init__()
        print("construtor da derivada")

    def metodo(self):
        super().metodo()
        print("metodo derivada")

    def funcao(self):
        print(super().funcao())
        return "funcao derivada"

    def __del__(self):
        super().__del__()
        print("destrutor derivada")

d = derivada()
print(d.atributo)
d.metodo()
print(d.funcao())
del d

