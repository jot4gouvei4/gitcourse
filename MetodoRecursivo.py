class laco:
    def repetir(self, inicio=0, fim=0, incremento=1):
        if inicio <= fim:
            print(inicio)
            inicio += incremento    # += para adicionar e manter
            self.repetir(inicio, fim, incremento)

laco = laco()
laco.repetir(0, 9, 1)

#laço de repetição resulta em 0-9

class laco:
    def repetir(self, inicio=0, fim=0, incremento=1):
        if inicio <= fim:
            print(inicio)
            inicio += incremento    # += para adicionar e manter
            self.repetir(inicio, fim, incremento)

laco = laco()
laco.repetir(0, 9, 1)
print()
laco.repetir(fim=9)   #usando apenas o parametro "fim"