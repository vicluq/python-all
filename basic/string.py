### Strings

## Metodos e funcoes
    # lower / uper / Title (esse ultimo deixa as primeiras letras maiúsculas)
    # format
    # F-string
    # len

## len
# Por baixo, como tudo em py é objeto, len(str) faz str.__len__ e retorna
password = input("Type your password: ")

if len(password) < 6:
    print("Invalid password")
else:
    print("Valid password")
    
# OBS: não usar isso para ordenar alfabeticamente duas strings pelo amor de deus
print("Ana Júlia" > "Vick") # Falso pois alfabeticamente, o primeiro nome é menor

## ljust e rjust -> bota o name em um dos lados e preenche até completar os N chars
name = "Luquetinha"
nameL = name.ljust(20, '*') # Justifica o nome à esquerda e preenche o resto com * ate chegar em 20
nameR = name.rjust(20, '*')

## INDEXES -> Cada char tem um índex e podemos manipular só o char e afins
word = "opa meu jovem"
counter = -1 # -1 pois o primeiro char começa com 0 (index 0)

for c in word:
    ++counter
    print(c)
    if c == 'o':
        print("Found an O!")

## Extraindo substrings -> str[start:end:step]
size = len(word)
subWord = word[0:4] # var[start:end] - é igual a JS, ele não pega o end mas o anterior 
subWord = word[0:6:3]
subWord = word[5:] # sem não passar nada ele pega daquele ponto até tudo ou a partir do 0 até onde pedi
subWord = word[:(size - 1)] # 
print(subWord)
# índices negativos -> o ultimo char sempre começa no -1 e segue