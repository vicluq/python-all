# NOTE Lambda
    # funções anônimas, tipo arrow function, mas mais curtas ainda, pois só são one line e já retornam o valor

anonymousFunc = lambda n1, n2: n1 / n2 if (not n2 == 0) else Exception("Cannot perform the division")
print(anonymousFunc(2, 0))
print(f"{anonymousFunc(2, 3):.2f}")

# NOTE Usos lambda
listaPessoas = [
    {"nome": "Victoria", "idade": 21},
    {"nome": "Lucas", "idade": 23},
]

# Retorno a key que o python vai usar para comparar cada elemento
listaPessoas.sort(key=lambda d: d['nome'])
sortedByName = sorted(listaPessoas, key=lambda d: d['idade'])

# NOTE *args e **kwargs
    # ! Desempacotamento review 

