#Associação é a capacidade de associarmos uma classe a outra

class filhos:
    nomes = ['josé', 'mario', 'duda']

class pessoa:
    nome = 'joao'
    idade = 40
    salario = 5200
    f = filhos()

p = pessoa()
nome = p.nome
idade = p.idade
salario = p.salario
f = p.f.nomes

print('informacoes pessoais')
print()
print(f'Nome: {nome}')
print(f'Idade: {idade} anos')
print(f'salario: R$ {salario}')
print()
print('Filhos:')
for filho in f:
    print(filho)
