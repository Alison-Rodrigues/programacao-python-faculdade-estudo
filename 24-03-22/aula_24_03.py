palavra = input("Digite uma palavra: ")
letra = input("Digite a letra que você quer procurar: ")

#Pesquisa a posição da primeira ocorrência da esquerda para a direita
print("Pesquisa a posição da primeira ocorrência da esquerda para a direita")
print(palavra.find(letra))

#Pesquisa a posição da última ocorrência da direita para a esquerda
print("Pesquisa a posição da última ocorrência da direita para a esquerda")
print(palavra.rindex(letra))

#Transforma a palavra em caixa alta
print("Transforma a palavra em caixa alta")
print(palavra.upper())

#Transforma a palavra em caixa baixa
print("Transforma a palavra em caixa baixa")
print(palavra.lower())


#Troca a letra escolhida
trocaLetra = input("Digite a letra para trocar trocar: ")
print("Troca a letra escolhida")
print(palavra.replace(letra, trocaLetra))
