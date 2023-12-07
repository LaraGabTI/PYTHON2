#CRUD - created, readed, updated e deleted

#created
dic = {'nome' : 'Paulo'} 
dic2 = dict(idade=23)

#readed
dic['nome']
reading = dic2.get('idade')

#updated
dic.update(sobrenome = 'Junior')
#add dic no meu dic
dic.update({'idade' : 23}) 
#pra add uma tupla ou lista(iteravel) tem que colocar virgula no final
tupla = ('peso', 72.12),
dic.update(tupla)
#add lista
lista = ['data', '13/04/1996'],
dic.update(lista)
print(dic, dic2)