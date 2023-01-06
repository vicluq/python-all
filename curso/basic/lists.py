''' NOTE listaAS '''
    # São arrays dinâmicos (listaa linkada), tipo em JS, criamos colocando  os colchetes
    # Acessamos via indexação 0 à size - 1
    # tamanho da listaa com len(lista)
    # Diferente de string, são mutáveis e podemos fazer lista[n] = x
    # também suportam fatiamento lista[start:end:step]
    # append, insert(index, elem), pop, del, clear, extend (concat uma listaa com a que chamou o método), etc
    # min, max(lista) -> pegar o maior e o menor valor da listaa
    # range
    # count(valor) -> quantos desse valor aparece na lista
    # list.sort(key=, reverse=)
    # sorted(list, key=, reverse=)

# Basic
empty_lista = [] # listaa vazia
lista = [1, 55, 3.4, "ola"] # uma listaa pode conter qualquer coisa (recomendado não fazer isso)
names = ["Vic", "Luquet", "Victoria"]

# NOTE Concatenação
concat = lista + names # (1)

concat = [] + lista # (2)
concat.extend(names)

print(lista, lista[len(lista) - 1], names[1:3], concat, sep='\n')

# NOTE Inserindo e removendo
lista.insert(2, 3.47) # insere onde quero
names.append("quets") # insere ao final da listaa

lista.pop(2) # Removendo do index 2 (se eu n passar nada, o pop remove do fim)
del(lista[2:4]) # Deleta lista[2] e lista[3]

print(lista)

# NOTE Funções min e max
lista = [1, 55, 2, 98, 4, 55, 78, 32, 28]
maxlista = lista[0] # max(lista)
minlista = lista[0] # min(lista)

for n in range(1, len(lista)): # o for in também serve com listas (por baixo uma string eh uma lista de chars)
    if lista[n] > maxlista:
        maxlista = lista[n]
    elif lista[n] < minlista:
        minlista = lista[n]

print(lista, f"max = {maxlista}", f"min = {minlista}", sep='\n')

# NOTE Criando uma lista com range
impares = list(range(1, 11, 2)) # lista() converte o objeto iterável que passamos em listaa
print(impares)

impares.insert(10, 17) # se eu tentar add em um index que seja maior que o tamanho da lista, ela faz append

### NOTE Enumerate -> enumera a lista e nos fornece o index em loops
    # Não serve só para listas, ela enumera voltas do laço tbm, retornando uma tupla [volta, value], podendo usar com range e iteráveis no geral
sentence = "Victoria é muito fofa"
wordList = sentence.split(" ")
word = ""
for index, value in enumerate(wordList):
    if index % 2 == 0:
        word += value

### NOTE Lista dentro de lista
matrix = [ [3, 55], [3.76, 145] ]
enumerateResult = enumerate(matrix)
print(enumerateResult)

# O loop pode ter mais params, tipo: 
for val1, val2 in matrix:
    print(val1, val2) # desempacotando os subarrays

### NOTE Desestruturando listas
w1, w2, w3, w4 = wordList

# Eu não posso desempacotar com menos variáveis que a lista tem de elementos, logo uso assim com o asterisco:
w1, w2, *otherWords = wordList # otherWords é uma lista com o resto
print(otherWords)

# ! o * e o ** sao equivalentes ao rest do JS, mas o primeiro pra lista e o segundo pra dict e obj