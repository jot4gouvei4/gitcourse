class classe:
    def funcao1(self):
        return "retorno funcao1"

    def funcao2(self):
        return self.funcao1()

    def funcao3(self):
        return self.funcao2()

c = classe()
print(c.funcao3())




#Alternativa 1


class classe:
    def funcao1(self, msg):
        return msg

    def funcao2(self, msg):
        return self.funcao1(msg)

    def funcao3(self, msg):
        return self.funcao2(msg)

c = classe()
print(c.funcao3("retorno primeira funcao"))


#Alternativa 2

class classe:
    def funcao1(self):
        return "retorno da primeira funcao"

    def funcao2(self):
        return self.funcao1()

    def funcao3(self):
        return self.funcao2()
    def funcao4(self):
        return self.funcao3()
c = classe()
print(c.funcao4())

