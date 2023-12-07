dic = {'lara' : '123',
       'paula' : '456',
       'alice' : '789', }
print(dic)


usuario = input('Digite seu login')
senha = input('Digite a senha')  


dic_login = {}
dic_login[usuario] = senha
print(dic_login)


for chave in dic.keys():
    if chave == usuario:
        print('Usuario ok')
        if dic[chave] == dic_login[usuario]:
            print("Voce esta logado")
            break
        else:
            print('Voce errou a senha')
            break
else:
    print('usuario incorreto')

'''for chave in dic.keys(): #pegando os nomes
    if dic[chave] == dic_login[usuario]:
        print (chave, dic_login[usuario])'''


