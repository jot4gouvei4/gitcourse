class classe:
    atributo = "valor padrão"

c = classe()
print(c.atributo)


class classe1:
    def __init__(self):
        self.atributo = "valor padrão1"

c = classe1()
print(c.atributo)


class classe2:
    atributo = "valor padrão2"
    
    def __init__(self):
        self.atributo = "outro valor"


c = classe2()
print(c.atributo)


class classe3:
    def __init__(self):
        self.atributo = "valor padrão3"
    
    def funcao (self):
        self.atributo = "valor atualizado"
        return self.atributo

    def metodo(self):
        print (self.atributo)

        
     
c = classe3()
print(c.atributo)
retorno = c.funcao()
c.metodo()
print(retorno)
