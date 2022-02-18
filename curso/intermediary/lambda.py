# NOTE Lambda -> funções anônimas, tipo arrow function, mas mais curtas ainda, pois só são one line e já retornam o valor

anonymousFunc = lambda n1, n2: n1 / n2 if (not n2 == 0) else "Cannot perform the division"
print(anonymousFunc(2, 0))
print(f"{anonymousFunc(2, 3):.2f}")