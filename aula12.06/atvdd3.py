nome = input('Seu nome: ')
idade = input('Sua idade: ')
aniversario = input('Seu aniversario: ')
bairro= input('Seu bairro: ')
rua = input('Suu rua: ')
numero = input('Numero da casa: ')


clientes_lista = [['nome', nome], ['idade:', idade],
                   ['aniversario:', aniversario], 
                   ['rua:' , rua], ['numero:', numero], ['bairro', bairro]]
print(clientes_lista)

clientes_dic = {}
clientes_dic.update(clientes_lista)
print(clientes_dic)