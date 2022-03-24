"""
Procurar a última ocorrência de um carácter num texto. 
A primeira linha será um texto grande. 
Seguido da letra que quer procurar. 
O sistema deve retornar a posição da última ocorrência.

"""

palavra = input("Digite uma palavra: ")
letra = input("Digite uma letra para procurar sua posição: ")
contador = 0
tamanho = len(palavra) - 1

while(tamanho > 0):
    
    if(palavra[tamanho] == letra):
        print(palavra)
        print(tamanho)
        break

    tamanho -= 1