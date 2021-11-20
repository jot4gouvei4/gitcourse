class classe:
    def metodo_principal(self, msg):
        def metodo_secundario(msg):
            print(msg)

        metodo_secundario(msg)

c = classe()
c.metodo_principal("mensagem teste")