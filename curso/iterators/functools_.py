from functools import partial
from itertools import reduce
from types import GeneratorType # Tipos alem dos padroes

# NOTE Map e filter podem ser feitos com list comprehension

# NOTE Map -> mesma ideia do JS, sendo q recebe o elemento iteravel a ser mapeado tb pq eh funcional
lista = [
    {'nome': 'Victoria', 'idade': 21}
]

# Retorna um iterator que é esgotado no uso
# logo, pra preservar e não perder as referencias, converte logo pra lista
new_lista = list(map(
    lambda d: {**d, 'idade': d['idade'] + 1},
    lista
))

# NOTE Filter -> mesma ideia do map, sendo que a funcao deve retornar im boolean pra se o elemento continua ou nao

# Retorna um iterator que é esgotado no uso
# logo, pra preservar e não perder as referencias, converte logo pra lista
filtered_lista = list(filter(
    lambda p: p['idade'] > 17,
    lista
))

# NOTE Reduce -> reduz um iteravel a um valor
    # Mesma ideia do JS -> passo uma funcao que recebe o acumulador e o elemento atual e retorno o novo valor do acumulador
    
soma_idades = reduce(
    lambda count, p: count + p['idade'],
    lista,
    0 # Valor inicial do acumulador
)