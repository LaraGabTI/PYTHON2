'''
• Escreva um código que, recebe três palavras e uma frase, 
crie uma função que verifique se as palavras aparecem COMPLETAS na frase e 
indique qual intervalo de índices ele foi encontrada. Você deve utilizar uma lista
para realizar a atividade.

Obs.: você deve validar se a palavra tem três ou mais letras
Obs.: você deve validar se a frase tem pelo menos 20 palavras '''

def frase_completa(palavras, frase):
    for p in palavras:
        achei = frase.find(p)
        tamanho = len(p) - 1
        if(achei >= 0):
            print(f"expressao encontrada no indice{achei} até o indice {achei+tamanho}")
        else:
            print("Expressão n foi encontrada na frase")


palavras = []
for i in range(3):
    palavra = input(f'Escreva a {i} palavra: ')
    while len(palavra) < 3:
        palavra = input("Digite a palavra novamente com mais de 3 caractere: ")
    else:
        palavras.append(palavra)
print(palavras)    

frase = input("Digite uma frase: ")
while len(frase) < 20:
    frase = input("Digite a palavra novamente com mais de 3 caractere: ")

frase_completa(palavras, frase)

