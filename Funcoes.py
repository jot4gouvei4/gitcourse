class classe:
    def funcao(self):
        return "retorno"

c = classe()
retorno = c.funcao()
print(retorno)

# Alternativa1

class classe:
    def funcao(self):
        return "retorno"

retorno = classe().funcao()
print(retorno)

# Alternativa2

class classe:
    def funcao(self):
        return "retorno"

retorno = classe.funcao(None)
print(retorno)

# Adição

class soma:
    def somar (self, x, y):
        resultado = x + y
        return resultado

s = soma()
print (f"2+3 = {s.somar(2,3)}")


# Subtração

class subtracao:
    def subtrair (self, x, y):
        resultado = x - y
        return resultado

s = subtracao()
print("3 - 2 = "+str(s.subtrair(3, 2)))


# Cálculos

class calculos:
    def adicao(self, x, y): return x + y
    def subtracao(self, x, y): return x - y
    def divisao(self, x, y): return x / y
    def multiplicacao(self, x, y): return x * y

c = calculos()
n1 = 10
n2 = 2
somar = c.adicao(n1, n2)
subtrair = c.subtracao(n1, n2)
dividir = c.divisao(n1, n2)
multiplicar = c.multiplicacao(n1, n2)

print (f"{n1} + {n2} = {somar}")
print (f"{n1} - {n2} = {subtrair}")
print (f"{n1} / {n2} = {dividir}")
print (f"{n1} * {n2} = {multiplicar}")