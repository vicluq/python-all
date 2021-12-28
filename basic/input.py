# função input -> pega o que é digitado pelo user e que está no buffer stdin

course = input("What is your course?\n") # Recebe uma string a ser exibida de prompt
print(f"The course is {course}")

# A função sempre retorna string, logo, precisamos fazer um casting
op1 = input("digite o primeiro op: ")
op2 = input("digite o segundo op: ")
print(float(op1) + float(op2)) # soma normal pois houve o cast
print(op1 + op2) # concatena os operadores pois são strings

op3 = float(input("digite o terceiro op: ")) # fazer o cast direto assim é bem tbm
print(float(op1) + float(op2) + op3)