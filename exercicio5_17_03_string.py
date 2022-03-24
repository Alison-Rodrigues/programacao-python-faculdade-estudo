palavra = input("Digite uma palavra: ")
letra = input("Digite a letra que você quer pesquisar? ")
tamanho = len(palavra) - 1
contador = 0
quantidadeLetra = 0

while(contador <= tamanho):
    if(palavra[contador] == letra):
        quantidadeLetra += 1
    contador += 1

print(quantidadeLetra)