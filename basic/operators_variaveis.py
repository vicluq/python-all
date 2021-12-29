###  Operadores -> +, -, /, **, //, %, ()
# Exponenciação -> **
# Divisão arredondada p/ inteiro -> //
# Precedência: Parenteses -> Potencia/Raíz -> Multiplicação/divisão e módulo -> Add e Sub
# Se eu quiser repetir uma string ou char muitas vezes, basta fazer uma multiplicação pelo num que quero

print("Multiplicação com string:")
print(3 * "Vic Luq\n")

# limitar num de casas decimais
result = 10 / 3
print(round(result, 2))  # round(num, casas)
print(f"{result:.2f}")  # Parecido com C (só rola com interpolação)

### Operadores relacionais -> ==, <=, >=, !=, >, <

### Básico de Formatando string
myString = "Hello, Peter"
age = 16

# Interpolação de string com o "f"
banco = 122
print(f"tenho R${banco} no banco")
print(f'tenho R${banco} no banco')  # serve com single quotes tbm

# Função Format 
# os brackets funcionam como identificadores de forma que ele bota na ordem que as vars são dadas
print("Frase: {}\nIdade: {}".format(myString, age))
# funciona com parâmetros (não precisa ser na ordem mais)!!
print("Frase: {strn}\nIdade: {i}".format(i = age, strn = myString)) 
