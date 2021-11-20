class classe:
    def __init__(self):
        print("classe acessada")

    def metodo(self):
        print("metodo iniciado")

    def __del__(self):
        print ("classe descarregada da memoria")

c = classe()
c.__init__()
c.metodo()
c.__del__()
del c
