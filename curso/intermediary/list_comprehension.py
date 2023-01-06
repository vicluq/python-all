# NOTE Criar listas com uma linha só e usando condicoes
    # Usamos um iterável para produzir os elementos (range, etc)

lista = [x for x in range(10)] # adiciona x para todo x no range

# NOTE Criando com base em outra lista
lista1 = [1, 2, 3, 4, 5, 7]
lista2 = [x for x in lista1] # Copiando a lista
print(lista2)

# NOTE Com operacoes
listaPor2 = [y * 2 for y in lista1]
print(listaPor2)

# NOTE Com dicionários / OBJ
pessoas = [
    {'nome': 'Victoria', 'idade': 21},
    {'nome': 'Julia', 'idade': 19},
    {'nome': 'Gustavo', 'idade': 20},
    {'nome': 'Pedro', 'idade': 17},
]

nomesPessoas = [
    p['nome']
    for p in pessoas
]

print(nomesPessoas)

# NOTE Com condicoes (usamos ternário)
listaDiv2 = [
    num // 2
    if num % 2 == 0 else num
    for num in lista1
]

print(listaDiv2)

# NOTE Mapeamento de listas
pessoasComSalario = [
    { **p, 'amount': p['idade'] * 100 }
    if isinstance(p['idade'], int) else { **p, 'amount': int(p['idade']) * 100 }
    for p in pessoas
]
# ? isinstance -> checa o tipo do elemento, a classe a qual ele pertence. ex: isistance(elem, type)

print("PESSOAS COM SALARIO", *pessoasComSalario, sep='\n')

# NOTE Filter de listas
    # Na filtragem, o if vem depois do for, x para todo x em iter SE x alguma coisa
    
pessoasDeMaior = [
    { **pessoa }
    for pessoa in pessoas
    if pessoa['idade'] > 17
]

pessoasComSalario = [
    { **p, 'amount': p['idade'] * 100 }
    if p['idade'] * 100 > 1000 else { **p, 'amount': p['idade'] * 150 } # * Cond de map
    for p in pessoas
    if p['idade'] > 17 # * Cond de filtro
]

# NOTE Mais de um for
todasDuplasPossiveis = [
    (x, y)
    for x in range(4) # para cada x ele roda o for do y
    for y in range(2)
]

# NOTE Fazendo uma matriz
matriz = [
    [x for y in range(3)]
    for x in range(3) # vai criar 3 linhas com 3 colunas do mesmo valor x
]