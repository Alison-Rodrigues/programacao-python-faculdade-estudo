#Criar um novo String formado pela última e primeira letra de uma palavra.

palavra = input("Digite uma palavra: ")
tamanho = len(palavra)

print(f"{palavra[tamanho - 1]}{palavra[0]}")
