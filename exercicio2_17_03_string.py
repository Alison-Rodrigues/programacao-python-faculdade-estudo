"""
Criar um novo String formado pelas três letras do meio de uma palavra. 
Cada palavra deve conter pelo menos 3 letras.

"""

palavra = input("Digite uma palavra: ")
tamanho = len(palavra)

print(f"{palavra[tamanho // 2 - 1]}{palavra[tamanho // 2]}{palavra[tamanho // 2 + 1]}")