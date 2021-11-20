#Ex. 1:

class classe1:
    def metodo(self):
        print("sem msg")

class classe2(classe1):
    def metodo(self, msg=""):
        if len(msg.strip()) == 0:
            super().metodo()
        else:
            print(f"mensagem recebida: {msg}")

c = classe2()
c.metodo()
c.metodo("teste")



#Ex. 2:

class classe1:
    def metodo(self, string= ""):
        print(f"o parametro é string: {string}")

class classe2(classe1):
    def metodo(self, parametro=""):
        if type(parametro) == str:
            super().metodo(parametro)
        
        else:
            print(f"não é string: {parametro}")

c = classe2()
c.metodo("texto")
c.metodo(5)

