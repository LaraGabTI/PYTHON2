dic = {'lara' : '123',
       'paula' : '456',
       'alice' : '789', }
print(dic)


usuario = input('Digite seu login')
senha = input('Digite a senha')  

dic_login = {usuario:senha}
'''
for k, v in dic.items():
    if usuario == k:
          
        if senha == v:
            print('logado')
        else:
            print('voce errou a senha')
   
    else:
        print('voce errou o login')'''
for chave in dic.keys():
    if dic[chave] == dic_login[usuario]:
        print (chave, dic_login[usuario])

