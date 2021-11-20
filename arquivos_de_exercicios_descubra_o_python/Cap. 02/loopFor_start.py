#
# Arquivo com exemplos de Loops
#

# Definindo um LOOP FOR

def LoopFor ():
    for x in range(5, 10):
        print (x)

LoopFor()


# Usando um LOOP FOR em uma coleção

def LoopArray ():
    dias = ["seg", "ter", "quar", "quin", "sex", "sab", "dom"]
    for d in dias:
        print (d) 
LoopArray()

# Usando BREAK e CONTINUE


# Usando a função enumerate, paara buscar valoeres e seus índices


def LoopEnum ():
    dias = ["seg", "ter", "quar", "quin", "sex", "sab", "dom"]
    for i,d in enumerate(dias):
        print (i, d) 
LoopEnum()