#
# Exemplo de como usar os comando Break e Continue
#
def LoopBreak():
    for x in range(5, 10):
        if x == 7:
            break
        print ("o valor de x é : ", x)

LoopBreak()

#LoopBreak()

def LoopContinue():
    for x in range(5,10):
        if x==7:
            continue
        print ("o valor de x é ", x)

LoopContinue()
