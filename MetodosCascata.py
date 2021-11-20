class classe:
    def metodo1 (self, msg):
        print (msg)

    def metodo2 (self, msg1, msg2):
        self.metodo1(msg1)
        print (msg2)

    def metodo3 (self, msg1, msg2, msg3):
        self.metodo2(msg1, msg2)
        print(msg3)

c = classe()
c.metodo3("primeiro", "segundo", "terceiro")

