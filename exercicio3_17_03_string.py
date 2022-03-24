"""
Procurar a primeira ocorrência de um carácter num texto. 
A primeira linha será um texto grande. 
Seguido da letra que quer procurar. 
O sistema deve retornar a posição da primeira ocorrência.

"""

palavra = input("Digite uma palavra: ")
letra = input("Digite uma letra para procurar sua posição: ")
contador = 0
tamanho = len(palavra) - 1

while(contador <= tamanho):
    
    if(palavra[contador] == letra):
        print(f"{contador}")
        break

    contador += 1