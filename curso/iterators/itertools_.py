from itertools import count, combinations, permutations, product, groupby
# NOTE Count -> contador infinito (range sem fim) e é um iterador
    # Toda vez que chamamos o next nele, ele entrega o valor e soma +1

cont = count()
cont2 = count(start=5, step=5) # passei nomeado só pra ver quais os param

for num in cont:
    if num > 15:
        break
    print(num)

# NOTE Cominacoes -> montar as combinacoes de uma lista
    # Ordem nao importa pois, nesse caso, (1, 2) == (2, 1)
    
pessoas = ["Victoria", "Julia", "Maria", "Tiago"]
combinacoes = combinations(pessoas, 2) # Combinar as pessoas em duplas

print(list(combinacoes))

# NOTE Permutacao -> a ordem importa
    # Queremos fazer um podio de 3 lugares por ex
    # A lista tem 4 pessoas, logo a permutacao seria 4 * 3 * 2
    
permuts = permutations(pessoas, 3)

# NOTE Product -> faz o produto cartesioano de 2 ou mais listas de uma lista

# NOTE Group by -> agrupa valores repetidos ou por uma chave de uma lista
    # Os dados PRECISAM estar ordenados
    # para agrupar um dic ou obj pela chave, é a mesma ideia do srot pela key
    # groupby(list, key=lambda d: d[key])