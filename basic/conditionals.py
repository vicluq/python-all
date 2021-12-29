# IF, ELIF, ELSE
    # Python usa identacao com dois pontos e nao chaves

name = input("what is your name?\n")
isAdmin = False

# keyword [expression...]:
    # ident block

if name.lower() == "victoria": # lower() converte tudo para lowercase
    print("you have admin access!")
    isAdmin = True
else:
    print("you don't have admin access :(")
    isAdmin = False

# Operadores logicos
    # and -> && eh o 'e' logico
    # or -> || eh o 'ou' logico
    # not -> ! eh o 'nao' logico
    # in -> saber se algo ta presente em uma lista ou algo numa string
    # not in -> o mesmo de cima mas ao contrario

age = input("Type your age: ")

if age >= 18:
    print("You can drink alchol")
elif age < 18 and age >= 16:
    print("you can have a sip")
else:
    print("you can't have anything")

if name.lower() == "vic" or name.lower() == "luq":
    print("You are a root user")

isVin = ('vic' in name) # checa se a substring vic ta no nome