class mensagens:
    def metodo(self):
        print("metodo msg")

    def funcao(self):
        return "funcao chamada"

m = mensagens()
m.metodo()
print(m.funcao())


class divisao:
    def dividir(self, n1=0, n2=0):
        try:
            if n2 == 0:
                raise Exception("não é possivel dividir por zero")
            print(f"{n1} / {n2} = {n1/n2}")
        except Exception as erro:
            print(erro)

    def dividir2(self, n1=0, n2=0):
        try:
            if n2 == 0:
                raise Exception("não é possivel dividir por zero")
            return(f"{n1} / {n2} = {n1/n2}")
        except Exception as erro:
            return erro

d = divisao()
n1=10
n2=2
d.dividir(n1,n2)
print(d.dividir2(n1,n2))
print()     #pular linha
n1=10
n2=0
d.dividir(n1,n2)
print(d.dividir2(n1,n2))