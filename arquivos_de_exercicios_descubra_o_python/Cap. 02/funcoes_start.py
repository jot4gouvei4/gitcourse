#
# Arquivo com exemplos de funções
#

# definindo uma função básica
def funcao1():
    print("eu sou uma função")

funcao1()


# função que recebe argumentos
def func2(arg1, arg2):
    print(arg1 + " " + arg2)

func2 ("Jota", "Gouveia")


# função que retorna um valor
def cubo(x):
    return x * x * x

f = cubo (2)
print (f)
print (cubo(3))

def quadrado(y):
    return y * y

g = quadrado (5)
print (g)
print (quadrado(9))



