palavra = "Quets"
palavra_hidden = []
digitadas = []

for i in palavra:
    palavra_hidden.append('*') # Preencho com asteriscos
print(palavra_hidden)

while '*' in palavra_hidden:
    print('\n')
    letra = input("Digite uma letra: ")
    if letra in digitadas:
        print('Você ja digitou essa!')
    else:
        if letra in palavra.lower():
            digitadas.append(letra)
            for n in range(len(palavra)): # Caso a letra exista mais vezes
                if letra == palavra[n].lower() and palavra_hidden[n] == '*':
                    palavra_hidden[n] = letra
        else:
            print("Não tem essa letra")
            digitadas.append(letra)
    
    for c in palavra_hidden:
        print(c, end=" ")

    sabePalavra = input("Você sabe a palavra (y/n)? ")
    if sabePalavra == "y":
        tentativa = input("Digite a palavra: ")
        if tentativa.lower() == palavra.lower():
            print("Parabéns! Você acertou")
