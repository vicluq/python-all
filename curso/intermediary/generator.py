# NOTE Iterables
import sys
# Só sabem qual é o prox valor, n sabem o anterior, nem o ultimo nem nada
# Não sabe o tamanho nem nada, só o próximo

lista = [1, 3, 4, 6]
iterator = iter(lista)
# ! erro: len(iterator)

# * Apenas conhece o próximo valor, e avanca o ponteiro
next1 = next(iterator)
next2 = iterator.__next__()

# NOTE Generator expression
# É um iterable tbm, pois conseguimos dar um forward
# Ele pausa em algum momento e retoma quando eu pedir
# É uma forma de gerar grandes listas iteráveis mas aos poucos sem ocupar muito


lista = [x for x in range(10000)]  # Bota tudo de vez a mem
# Não guarda tudo na mem de vez, aos poucos
generator = (x for x in range(10000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
# Se eu aumentar o range, o generator fica com tamanho igual antes, pois ele vai até certo ponto, so continua se eu mandar
# Se eu pedir um valor, ai sim o generator carrega na memoria

# * Dito tudo: o generator não tem len, não tem index, pois não está na memória. Ele sabe o próx valor mas não sabe mais nada
# O bom é que podemos usar o for com ele e afins

# NOTE Generator functions
# Uma funcao que pode pausar a execucao e voltar quando eu quiser (pique a de JS)
# Keyword yield -> cada retorna o valor de yield
# * O retorno da funcao é um generator com os valores de yield -> chamamos em sequencia com o next
# O return para a execucao
# * Podemos usar para aguardar resultados de operacoes assincronas
# ? Funcionamento: pausa até encontrar um yield e quando achar um return, ele sai, ao chamar o next ele vai pro outro yield
# * yield from -> continua de onde outro generator parou


def gen_get_something():
    yield "I"  # Pausa aqui e retorna
    yield "yielded"  # Pausa aqui e retorna
    yield 'this'  # Pausa aqui e retorna

    return "acabou a execucao"


returnedGen = gen_get_something()

for word in returnedGen:  # Por baixo chama o next ai vai pro prox yield e quando nao tiver mais, acaba no return
    print(word)

# * Basicamente, a funcao so avanca para o proximo yield se eu pedir (chamar o next)
    # Como se ela tivesse la no background esperando eu ir pro prox yield
