import abc  #importar estruturas abstratas que devem ser declarados

class Interface(abc.ABC):
    @abc.abstractmethod
    def soma(self, n1=0, n2=0): pass #deverá exibir n1 + n2
    @abc.abstractmethod
    def subtracao(self, n1=0, n2=0): pass #deverá exibir n1 - n2    
    @abc.abstractmethod
    def divisao(self, n1=0, n2=0): pass #deverá exibir n1 / n2
    @abc.abstractmethod
    def multiplicacao(self, n1=0, n2=0): pass #deverá exibir n1 * n2

class Classe(Interface):
    def metodo(self):
        print("interface em orientacao a obj")
    def soma(self, n1=0, n2=0):
        return(f"{n1} + {n2} = {n1+n2}")
    def subtracao(self, n1=0, n2=0):
        return(f"{n1} - {n2} = {n1-n2}")
    def divisao(self, n1=0, n2=0):
        return(f"{n1} / {n2} = {n1/n2}")
    def multiplicacao(self, n1=0, n2=0):
        return(f"{n1} * {n2} = {n1*n2}")

c = Classe()
c.metodo()
print (c.soma(2,3))
print (c.subtracao(5,2))
print (c.divisao(10,2))
print (c.multiplicacao(2,4))
