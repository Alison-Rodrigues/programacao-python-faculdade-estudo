"""
Conferir se um texto seria um palíndromo. 
Palíndromo é uma palavra, frase ou número que permanece igual quando lida de trás para diante. 
Para cada linha inserida o sistema retornará se o texto é palíndromo ou não.

"""

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




