palavra = input("Digite uma palavra: ")
letra = input("Digite uma letra para procurar sua posição: ")
contador = 0
tamanho = len(palavra) - 1

while(contador <= tamanho):
    
    if(palavra[contador] == letra):
        print(f"{contador}")
        

    contador += 1