# NOTE Dict Comprehension
pessoa = {
    'nome': 'Victoria',
    'idade': 21,
    'curso': 'Eng. Computacao'
}

dic = {
    chave: valor
    for chave, valor in pessoa.items() # Rola qualquer iteravel que podemos obter uma chave e um valor
}

