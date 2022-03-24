def palindromo(texto):
    tamanho = len(palavra) - 1
    contador = 0
    
    while(contador < tamanho):
        posicaoInicial = palavra[contador]
        posicaoFinal = palavra[tamanho - contador]
        if(posicaoInicial != posicaoFinal):
            return False
        return True

palavra = input("Digite a palavra: ")

if(palindromo(palavra)):
    print("A palavra é palíndroma!")
else:
    print("A palavra não é palíndroma!")




