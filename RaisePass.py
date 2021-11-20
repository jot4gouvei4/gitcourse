class divisao:
    def dividir(self, n1=0, n2=0):
        try:
            if n2 == 0:
                raise Exception("divisão por 0")
            print (f"{n1}/{n2} = {n1/n2}")

        except Exception as e:
            print (e)

        else:
            print ("sem erro")

        finally:
            print ("semrpe executado")

d = divisao()
d.dividir(10)



class divisao1:
    def dividir(self, n1=0, n2=0):
        try:
            print (f"{n1}/{n2} = {n1/n2}")

        except:
            pass

d = divisao1()
d.dividir(10)



class divisao2:
    def dividir(self, n1=0, n2=0):
        try:
            print (f"{n1}/{n2} = {n1/n2}")

        except:
            pass

        else:
            pass

        finally:
            pass

d = divisao2()
d.dividir(10,2)

#pass é utilizado para ignorar estruturas de código vazias
