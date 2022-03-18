#printar apenas as 3 últimas letras

texto = input("Digite uma palavra: ")
tamanho = len(texto)
contador = tamanho - 3

while(contador < tamanho):
    print(texto[contador])
    contador += 1
