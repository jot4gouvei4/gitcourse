class classe:
    def metodo(self):
        print("metodo executado")

c = classe()
c.metodo()


class classe1:
    def __init__ (self):
        print ("construtor1 executado")

    def metodo (self):
        print ("metodo1 executado")

    def __del__(self):
        print ("destrutor1 executado")

c = classe1()
c.metodo()
del c


class classe2:
    def __init__ (self):
        print ("construtor2 executado")

    def metodo (self):
        print ("metodo2 executado")

    def __del__(self):
        print ("destrutor2 executado")

classe2.metodo(None)
classe2.__del__(None)
classe2.__init__(None)


class classe3:
    def metodo (self, msg):
        print (msg)


c = classe3()
c.metodo("olá!")




class classe4:
    def metodo (self, msg1, msg2):
        print (msg1)
        print (msg2)


c = classe4()
c.metodo("olá,", "tudo bem?")



class classe5:
    def metodo (self, msg1, msg2):
        print (msg1)
        print (msg2)


c = classe5()
c.metodo(msg2="tudo bem?", msg1="olá,")