class divisao:
    def dividir(self, n1=0, n2=0):
        try:
            print (f"{n1}/{n2} = {n1/n2}")

        except Exception as e:
            print (e)
        
        else:
            print("sem erro")
        
        finally:
            print("sempre executado")

#else só roda se não tive erro
#finally é executado de qualquer forma

d = divisao()
d.dividir(10, 2)