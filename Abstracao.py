#abstração = acessar conteudo de uma classe por meio de um objeto

class abstrair:
    atributo = 'atributo abstraído'
    def metodo(self):
        print("abstraído")
    def funcao(self):
        return 'funcao abstraída'

abstracao = abstrair()
print(abstracao.atributo)
abstracao.metodo()
print(abstracao.funcao())

