class classe:
    def metodo1(self):
        print ("metodo1")

    def metodo2(self):
        self.metodo1()
        print ("metodo2")

c = classe()

c.metodo2()


class classe1:
    def metodo(self):
        print ("metodoC1")

class classe2:
    def metodo(self):
        print ("metodoC2")

    def metodoprincipal(self):
        classe1().metodo()
        self.metodo()

c2 = classe2()
c2.metodoprincipal()


#de outra maneira


class classe1:
    def metodo(self):
        print ("metodoC1")

class classe2:
    def metodo(self):
        print ("metodoC2")

    def metodoprincipal(self):
        classe1.metodo(self)
        self.metodo()

c2 = classe2()
c2.metodoprincipal()