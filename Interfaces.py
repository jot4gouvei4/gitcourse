#Ex. 1:

class interface:
    def soma(self, n1=0, n2=0): pass #deverá exibir n1 + n2
    def subtracao(self, n1=0, n2=0): pass #deverá exibir n1 - n2    
    def divisao(self, n1=0, n2=0): pass #deverá exibir n1 / n2
    def multiplicacao(self, n1=0, n2=0): pass #deverá exibir n1 * n2

class classe(interface):
    def metodo(self):
        print("interface em orientacao a obj")

c = classe()
c.metodo()


#Ex. 2 (design Petternes):

class interface:
    def soma(self, n1=0, n2=0): pass #deverá exibir n1 + n2
    def subtracao(self, n1=0, n2=0): pass #deverá exibir n1 - n2    
    def divisao(self, n1=0, n2=0): pass #deverá exibir n1 / n2
    def multiplicacao(self, n1=0, n2=0): pass #deverá exibir n1 * n2

class classe(interface):
    def metodo(self):
        print("interface em orientacao a obj")

    def soma(sel, n1=0, n2=0):
        print(f"{n1} + {n2} = {n1+n2})")
    def subtracao(sel, n1=0, n2=0):
        print(f"{n1} - {n2} = {n1-n2})")
    def multiplicacao(sel, n1=0, n2=0):
        print(f"{n1} * {n2} = {n1*n2})")
    def divisao(sel, n1=0, n2=0):
        print(f"{n1} / {n2} = {n1/n2})") 

c = classe()
c.metodo()
c.soma(2, 3)
c.subtracao(5, 2)
c.multiplicacao(2, 5)
c.divisao(4, 2)



#Ex. 3 (com funções):

class interface:
    def soma(self, n1=0, n2=0): pass #deverá exibir n1 + n2
    def subtracao(self, n1=0, n2=0): pass #deverá exibir n1 - n2    
    def divisao(self, n1=0, n2=0): pass #deverá exibir n1 / n2
    def multiplicacao(self, n1=0, n2=0): pass #deverá exibir n1 * n2

class classe(interface):
    def metodo(self):
        print("interface em orientacao a obj")

    def soma(sel, n1=0, n2=0):
        return f"{n1} + {n2} = {n1+n2})"
    def subtracao(sel, n1=0, n2=0):
        return f"{n1} - {n2} = {n1-n2})"
    def multiplicacao(sel, n1=0, n2=0):
        return f"{n1} * {n2} = {n1*n2})"
    def divisao(sel, n1=0, n2=0):
        return f"{n1} / {n2} = {n1/n2})"

c = classe()
c.metodo()
print(c.soma(2, 3))
print(c.subtracao(5, 2))
print(c.multiplicacao(2, 5))
print(c.divisao(4, 2))