class sobrecarga:
    def __init__(self, numero):
        self.numero = numero
    
    def __add__(self, outro_numero):
        return self.numero + outro_numero.numero
    
    def __sub__(self, outro_numero):
        return self.numero - outro_numero.numero
    
    def __truediv__(self, outro_numero):
        return self.numero / outro_numero.numero

    def __mul__(self, outro_numero):
        return self.numero * outro_numero.numero    

    def __mod__(self, outro_numero):
        return self.numero % outro_numero.numero

s1 = sobrecarga(4)
s2 = sobrecarga(2)

add = s1 + s2
sub = s1 - s2
div = s1 / s2
mul = s1 * s2
mod = s1 % s2   # Resto = %

print(f"4 + 2 = {add}\n4 - 2 = {sub}\n4 / 2 = {div}\n4 * 2 = {mul}\n4 % 2 = {mod}")
# Sobrecarga de Operadores
# Pular linha = \n