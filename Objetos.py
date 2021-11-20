class instancia:
    def __init__ (self):
        print ("classe instanciada")

    def metodo (self, msg):
        print(msg)

    def funcao (self):
        return "função executada"

objeto = instancia()
objeto.metodo("olá")
retorno = objeto.funcao()
print(retorno)
