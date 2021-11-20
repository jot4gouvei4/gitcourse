#Executar metodos e funções de maneira diferente, de acordo com os parâmetros

#Ex. 1:
class classe:
    def metodo(self, msg=""):
        if len(msg.strip()) == 0:
            print("sem msg")
        else:
            print(f"mensagem exibida: {msg}")

c = classe()
c.metodo()
c.metodo("teste")

#Ex. 2:
class classe:
    def metodo(self, parametro=""):
        if type(parametro) == str:
            print(f"é string': {parametro}")
        else:
            print(f"não é string: {parametro}")

c = classe()
c.metodo("texto")
c.metodo(5)


#Ex. 3:
class classe:
    def funcao(self, msg=""):
        if len(msg.strip()) == 0:
            return "sem msg"
        else:
            return f"mensagem exibida: {msg}"

c = classe()
print(c.funcao())
print(c.funcao("teste"))


#Ex. 4:
class classe:
    def funcao(self, parametro=""):
        if type(parametro) == str:
            return f"é string': {parametro}"
        else:
            return f"não é string: {parametro}"

c = classe()
print(c.funcao("texto"))
print(c.funcao(5))


#Ex. 5:

class calculos:
    def divisao(self, n1=0, n2=0):
        if type(n1) == int or type(n1) == float:
            if type(n2) == int or type(n2) == float:
                if n2 == 0:
                    print("não é possível dividir por 0")
                else:
                    print(f'{n1} / {n2} = {n1/n2}')
            else:
                print("parametro 2 precisar ser um numero")
        else:
            print("parametro 1 precisa ser um numero")

d = calculos()                    
d.divisao()
d.divisao(10)
d.divisao(n2=2)
d.divisao("texto", 2)
d.divisao(10, "texto")
d.divisao("texto", "texto")
d.divisao(10, 2)
