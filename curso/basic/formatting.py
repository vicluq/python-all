# Modificadores para formatação - o format e f-strings nos deixa formatar coisas
 # :s -> strings
 # :d -> inteiros
 # :f -> floats
 # :.nf -> n casas decimais
 # :[char pra colocar][< ou > ou ^][quantidade de casas]
    # > - adiciona os extras à esquerda 
    # < - adiciona os extras à direita 
    # ^ - adiciona os extras à esquerda e à direita
    #  
div = 12 / 9

# NOTE Formatação com casa decimal
print(f"{div:.2f}") 
print(f"{round(div, 2)}") 

# NOTE Formatação com casa decimal + caracteres -> vai add 0s até completar 10 chars à esquerda
print(f"{div:0>10.3f}") 

name = "Victoria Luquet"
print(f"{name:@>20}") # lembrando que ele adiciona o que falta para completar a quantiade char que dei 

course = "Engenharia da computação"
print("{1:->21} -> {0}".format(name, course)) # acessando os dados pelo indeice de cada var (lembrar que posso nomear também)

# NOTE Interpolacao
nome = "Luquet"
preco = 26.2313
frase = "%s cobra R$%.2f" % (nome, preco)
print(frase)

# NOME ljust e rjust -> bota o name em um dos lados e preenche até completar os N chars
nameL = name.ljust(20, '*') # Justifica o nome à esquerda e preenche o resto com * ate chegar em 20
nameR = name.rjust(20, '*')

