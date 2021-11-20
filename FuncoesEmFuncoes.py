class classe:
    def funcao1(self, msg):
         return "digo: "+msg

    def funcao2(self, msg):
         return self.funcao1(msg)

c = classe()
print (c.funcao2("olá!"))




class classe1:
    def funcao(self):
        return "funcao classe1"
        
class classe2:
    def funcao(self):
        return classe1().funcao()

c2 = classe2()
print(c2.funcao())


#opcao 2


class class1:
    def funcao(self):
        return "funcao classe1"
        
class class2:
    def funcao(self):
        return class1.funcao(self)

c2 = class2()
print(c2.funcao())


