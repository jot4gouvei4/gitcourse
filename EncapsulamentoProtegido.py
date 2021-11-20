#Encapsulamento é uma permissão de acesso a  determinado recurso de uma classe
#Permite que recursos sejam acessados por meio de um objeto instanciado
#Usado para dentro da propria classe ou para passar a uma classe filha
#Evitar acesso direto de fora da classe a recursos protegidos
#Inicia-se por " _ " seguido por uma letra

#Forma errada:
class classe:
    _atributo_protegido = "atributo protegido"
    def _metodo_protegido(self):
        print ("metodo protegido")

    def _funcao_protegida(self):
        return "funcao protegida"

c = classe()
print(c._atributo_protegido)
c._metodo_protegido()
print(c._funcao_protegida())


#forma correta:
class primaria:
    _atributo_protegido = "atributo protegido"
    def _metodo_protegido(self):
        print ("metodo protegido")

    def _funcao_protegida(self):
        return "funcao protegida"

class secundaria(primaria):
    atributo_publico = primaria._atributo_protegido
    def metodo_publico(self):
        self._metodo_protegido

    def funcao_publica(self):
        return self._funcao_protegida

s = secundaria()
print(s.atributo_publico)
s.metodo_publico()
print(s.funcao_publica())

