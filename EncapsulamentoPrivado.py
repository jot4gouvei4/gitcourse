#Encapsulamento privado impede que os recursos sejam acessados de fora da classe que o declarou
#"_ + _" no inicio, seguidos de letra


#errado
class classe:
    __atributo_privado = "atributo privado"
    def __metodo_privado(self):
        print ("metodo privado")

    def __funcao_privada(self):
        return "funcao privada"

c = classe()
print(c.__atributo_privado)
c._metodo_privado()
print(c.__funcao_privada())


#correto
class classe:
    __atributo_privado = "atributo privado"
    atributo_publico = __atributo_privado
    def __metodo_privado(self):
        print ("metodo privado")
    def metodo_publico(self):
        self.__metodo_privado()
    def __funcao_privada(self):
        return "funcao privada"
    def funcao_publica(self):
        return self.__funcao_privada()

c = classe()
print(c.atributo_publico)
c.metodo_publico()
print(c.funcao_publica())


#para uma classe filha acessar um encapsulameto privado da classe mãe deve-se relacionar com o correspondente publico que fizemos na classe mae
