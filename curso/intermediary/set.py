# NOTE Set
    # Não preserva a ordem dos elementos
    # Não tem index
    # Não aceitam valores mutaveis -> listas, dict, etc

# NOTE Criando Sets
mySet = set('Vic')
mySet = set([1,3,4,5,7])
# Passamos iteráveis pois o set desmembra eles em elementos imutáveis

myDefinedSet = {1, 3, 'Victoria'} # nesse caso, não desmembra a string

# NOTE Útil pra remover valores duplicados de iteráveis
myList = [2, 3, 4, 4, 6, 6]
mySet = set(myList)
myList = list(mySet)
# só cuidado pois o set não preserva a ordem

# NOTE podemos usar coisas de iteraveis (for, in, etc)
testSet = set([3, 5, 6, 2])
if 3 in testSet:
    print("3 esta no set")

# NOTE Métodos de set
# add
testSet.add(9)
# update -> concatena com os valores ja existentes
# clear -> limpa o set
# discard -> elimina o valor passado do set

# NOTE Operacoes úteis

# Uniao (set1 | set2)
# Intersecao (set1 & set2)
# Diferenca (set1 ^ set2)