class classe:
    def funcao_principal(self, msg):
        def funcao_secundaria(msg):
            return msg
        return funcao_secundaria(msg)

c = classe()
print (c.funcao_principal("valor de teste"))    


#2

class classe:
    def funcao_principal(self, msg):
        def funcao_secundaria(msg):
            def funcao(msg):
                return msg
            return funcao(msg)
        return funcao_secundaria(msg)

c = classe()
print (c.funcao_principal("valor de teste"))    