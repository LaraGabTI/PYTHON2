dic_perguntas = [{'Pergunta': "Qual é o animal nacional da Austrália?",
                 'Opcoes': ['aranha', 'canguru', 'onitorrinco', 'koala'],
                 'Resposta': "canguru"},
                 
                 {'Pergunta': "Quantos dias são necessários para a Terra orbitar o sol?",
                 'Opcoes': ['365', '30', '200', '300'],
                 'Resposta': "365"},
                 
                 {'Pergunta': "De qual cidade vieram os Beatles?",
                 'Opcoes': ['California', 'China', 'Canada', 'Brasel'],
                 'Resposta': "LivePoll"},
                 
                 {'Pergunta':"Onde foram realizados os primeiros Jogos Olímpicos modernos?",
                 'Opcoes': ['Egito', 'Africa', 'Atenas'],
                 'Resposta': "Atenas"},
                 
                 {'Pergunta':"Qual o nome do primeiro filme da Disney?",
                 'Opcoes': ['Branca de Neve', 'Cinderela', 'Bela e a Fera', 'Moana'],
                 'Resposta': "Branca de Neve"}]

#resposta = input(f'{dic_perguntas["Pergunta"]} {dic_perguntas["Opcoes"]}')
qtdd = 0
for pergunta in dic_perguntas:
    print(pergunta['Pergunta'])

    for i, opcoe in enumerate(pergunta['Opcoes']):
        print(f'{i+1}, {opcoe}')
    
    resposta = input('Digite sua resposta')  
    acertou = False
    # break
    if resposta == pergunta['Resposta']:
        acertou = True
        qtdd += 1
        print("Voce acertou")
    else:
        print("Errou")

print("")        
print("Fim de Jogo")
print(f'Voce acertou {qtdd} questoes')
    #resposta = input(f'[dic_perguntas{0}{0}] [dic_perguntas["Opcoes"]]')


#if(resposta == dic_perguntas['Resposta'][0]): 
#    print("voce acertou a questao")
#else:
#    print("tente novamente")
'''
#print(f'{dic_perguntas['Pergunta']} {dic_perguntas['Opcoes']}')
for c, v in dic_perguntas.items:
    print(f'{dic_perguntas["Pergunt]} {dic_perguntas['Opcoes']}')
    

'''
