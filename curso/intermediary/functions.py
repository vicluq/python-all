# NOTE Funções
# Para criar uma função, usamos a palavra def, seguido do nome da função e dos argumentos
# a jeyword return vai retornar um elemnto da função
# Se não enviarmos os parâmetros, vai dar um erro (existe um workaround)

def getSum(num1, num2):
    return num1 + num2

# NOTE Argumentos padrões para caso não envie algum valor
def getSub(num1=0, num2=0):
    return num1 + num2


getSub(3, 5)
getSub(3)
# Posso alterar a ordem em que recebe argumentos se eu nomear
getSub(num2=6, num1=4)


def talk(compliment="Hello", name="User"):
    print(compliment, name)


talk("")  # Valores falsy são contados cmo algo
talk("Opa!")


# NOTE Void -> retorna None por padrão (undefined em JS)

# NOTE -> Higher Order Functions -> retornam ou recebem funcoes

# NOTE Função retornando função -> func()() -> func retorna uma função e assim que chamamos ela
def funcToVar():
    print("Essa func ta em uma variável")

def retFunc():
    return funcToVar


varr = retFunc()  # Posso atribuit funções à variáveis
varr()  # == retFunc()()


# NOTE Podemos retornar n-tuplas
def tuplesFunc():
    return ("Luquets", "is", "nice")  # ou "Luquets", "is", "nice"


# NOTE *args -> quando não sabemos quantos argumentos teremos e a função fornece uma tupla args ('*' lembra ponteiro)
    # para converter pra lista -> args = list(args)
    # o spread de funções que nos da uma lista eh o *list em python -> posso desempacotar e mesclar listas assim
def sumNums(*args):
    result = 0
    for i in range(len(args)):
        result += args[i]
    return result

def complimentPeople(compliment, *args):
    # *args = list of people
    print(compliment + " " + " ".join(args))

print(sumNums(2, 6, 8, 90, 3))
complimentPeople("Parabens", "Victoria", "Julia", "Luis")

list1 = [4, 7, 2, 5]
list2 = [13, 7, 344, 90]
print(sumNums(*list1, *list2)) # desempacoto as listas e mesclo elas na tupla

# NOTE **kwargs -> argumentos com palavras chaves (com nomes atribuídos a eles). kwargs vira um tipo de objeto
    # kwargs.get(key) -> quando não temos certeza se existe a chave pra nao dar erro
    # kwargs[key] -> normal 
    # obs: a key deve ser uma string

def saudation(**kwargs):
    print(kwargs.get('msg'), kwargs['name'], kwargs.get('lastName'))

saudation(name = "Victoria", msg = "Hello", lastName = "Luquet")

# NOTE Keyword global para quando criarmos uma variável com o mesmo nome na função, tratarmos como se fosse a mesma do escopo global

def argumentos(*args, **kwargs):
    print(args)
    print(kwargs)

argumentos(4, 5, nome="Vic", idade=22)
argumentos(nome="Vic", idade=22)