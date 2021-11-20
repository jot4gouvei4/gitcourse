class divisao:
    def dividir(self, n1=0, n2=0):
        try:
            print (f"{n1}/{n2} = {n1/n2}")

        except:
            print ("erro")

d = divisao()
d.dividir(10, 2)
#se a divisão não for possível, aparece somente erro

class divisao:
    def dividir(self, n1=0, n2=0):
        try:
            print (f"{n1}/{n2} = {n1/n2}")

        except Exception as e:
            print (e)

d = divisao()
d.dividir(10)
#Exception retorna qual o erro