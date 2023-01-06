# Isso é um comment em py
'''
Isso é um comentário em bloco, o que na verdade é uma string não processada
'''

### NOTE Comando print
print("Victoria", "Luquet", sep=' ')
# Printa os argumentos que passamos
# sep é o saparador das strings/coisas passadas ao print
# end é o valor anexado no fim do último argumento
# ele printa arrays, objetos, strings e numeros

### NOTE Interpolação de string com o "f"
banco = 122
print(f"tenho R${banco} no banco")
print(f'tenho R${banco} no banco')  # serve com single quotes tbm

# Tipos de dados (variáveis sem tipagem especificada)
# str - string (podemos usar operadores +, <, >, == para concatenar e comparar)
# int - inteiros
# float - ponto flutuante
# bool - true e false (1 e 0)
# FALSY VALUES -> None, [], {}, "", 0
# None -> não valor

myINTvar = 13  # != '13'
myFLOATvar = 14.5
mySTRvar = "this is a name"
myBOOLvar = True  # =1

print(myBOOLvar == 0)  # Operação lógica de igualdade com variáveis

### NOTE Descobrindo o type das variáveis
print(type(myBOOLvar), type(myINTvar), sep='\n')
'''
Output:
<class 'bool'>
<class 'int'>
'''

# Casting -> uso o mesmo nome do tipo
someVar = 19
print(float(someVar))  # 19.0
print(str(someVar))  # 19 (porém string)

# OBS: só posso converter sse o dado for coerente né! tipo int("Luquet")

### NOTE Funções built in úteis de type

# Py não vai converter um tipo m outro para você que nem JS (str + num ele converte o num em str)
# nem sempre um dado entregue pelo user pode ser convertido em num, tipo "Vic", logo a gnt checa se é numérico, alfabético, etc

str1 = "1234"
str2 = "Victoria"
str3 = "2.55"

print(f"str: {str1} -> isdecimal: {str1.isdecimal()}, isnumeric: {str1.isnumeric()}, isdigit: {str1.isdigit()}")
print(f"str: {str2} -> isdecimal: {str2.isdecimal()}, isnumeric: {str2.isnumeric()}, isdigit: {str2.isdigit()}")
print(f"str: {str3} -> isdecimal: {str3.isdecimal()}, isnumeric: {str3.isnumeric()}, isdigit: {str3.isdigit()}")

# OBS: temo um problema com ponto flutuante... pois as funções checam se só há caracteres numéricos e pontos tão de fora

### NOTE Try Catch do python

try:
    num1 = float(input("Type num1: "))
    num2 = float(input("Type num2: "))

    print(num1 + num2)
except:
    print("Some error occured!")

# em caso de erro, ao invés de causar a parada do programa, executar o except

try:
    blabla = "2.55"
    int(blabla)
    print("Is convertable to int")
except:
    print("Not convertable to int")

# NOTE checkingif it is float
def is_float(num):
    try:
        int(num)
        return False # If convertable to int, returns false (not float)
    except:
        ...
    
    try:
        float(num)
        return True
    except:
        return False

print(is_float("2"))
print(is_float("2.24"))
print(is_float("Vick"))

# NOTE id -> o id da variável na memória, onde ela ta na memória
    # é como o python acha os elementos na memória
var = "Luquet"
print(id(var))