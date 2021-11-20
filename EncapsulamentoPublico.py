#Encapsulamento é uma permissão de acesso a  determinado recurso de uma classe
#Público pode ser acessado de qlqr parte do código
#Nome deve ser iniciado por uma letra

class classe:
    atributo_publico = "atributo publico"
    def metodo_publico(self):
        print ("metodo publico")

    def funcao_publica(self):
        return "funcao publica"

c = classe()
print(c.atributo_publico)
c.metodo_publico()
print(c.funcao_publica())
