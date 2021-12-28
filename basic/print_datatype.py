# Isso é um comment em py
'''
Isso é um comentário em bloco, o que na verdade é uma string não processada
'''

### Comando print
print("Victoria", "Luquet", sep=' ')
    # Printa os argumentos que passamos
    # sep é o saparador das strings/coisas passadas ao print
    # end é o valor anexado no fim do último argumento
    # ele printa arrays, objetos, strings e numeros

### Interpolação de string com o "f"
banco = 122
print(f"tenho R${banco} no banco")
print(f'tenho R${banco} no banco') # serve com single quotes tbm

### Tipos de dados (variáveis sem tipagem especificada)
    # str - string (podemos usar operadores +, <, >, == para concatenar e comparar)
    # int - inteiros
    # float - ponto flutuante
    # bool - true e false (1 e 0)

myINTvar = 13 # != '13'
myFLOATvar = 14.5
mySTRvar = "this is a name"
myBOOLvar = True # =1

print(myBOOLvar == 0) # Operação lógica de igualdade com variáveis

### Descobrindo o type das variáveis
print(type(myBOOLvar), type(myINTvar), sep='\n')
'''
Output:
<class 'bool'>
<class 'int'>
'''

### Casting -> uso o mesmo nome do tipo
someVar = 19
print(float(someVar)) # 19.0
print(str(someVar)) # 19 (porém string)

# OBS: só posso converter sse o dado for coerente né! tipo int("Luquet")