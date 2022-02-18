''' NOTE While  LOOPS

    while [condition]:
        code_block

    - Loop mais indicado pra fazer o loop infinito do programa
'''

num = int(input("Num to calc factorial: "))
backup = num
result = 1

while num > 0:
    result = result * num
    num = num - 1

print(f"factorial({backup}) = {result}")

## continue e break
    # o break sai do loop
    # o continue pula para a próxima iteração

num = backup
result = 1

while True:
    result = result * num
    num = num - 1
    if not num: # say do loop quando num = 0 pois 0 é falso
        break

print(f"factorial({backup}) = {result}")

while True:
    word = input("Digite uma palavra para saber o tamanho:\n")
    print("tamanho:", len(word))
    if word == '0':
        break;

''' NOTE FOR LOOPS '''

## For in loop -> faze loops em strings, listas
nome = "Victoria Luquetinha"
nomeReplaced = ''

for char in nome:
    if not char == 'i':
        nomeReplaced += char
    else:
        nomeReplaced += '1'


## for range -> combinar a função range com o for loop
    # range(start=0, stop, step=1) -> range(n) = start=0; stop=n; step=1

for i in range(5):
    print(i) # i vai de 0 a 4, pois o range segue a ideia de indexes (tipo extrair string)

for n in range(0, 11, 2):
    print(n) # pega apenas os pares de 1 até 10 pois vai de 2 em 2

for num in range(2, 101):
    prime = num
    div = 2
    
    while div < prime * prime: # div menores que a raiz do num 
        ...

## For / else -> um else pro for que é executado se o for ir até o fim, mas se houver breaks, ou parar antes, ele não é executado