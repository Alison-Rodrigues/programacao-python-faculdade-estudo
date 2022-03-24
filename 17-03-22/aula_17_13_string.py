#printar apenas a posição desejada da string

texto = input("Digite uma palavra: ")

print("Caractere na posição 2 da string:")
print(texto[2])

#printa o tamanho da palavra

print("Tamanho da string: ")
print(len(texto))

#printar apenas o último caractere

tamanho = len(texto)
print("Apenas o último caractere: ")
print(texto[tamanho - 1])

#printa os 3 últimos caracteres
print(texto[tamanho - 3 : tamanho])