# Strings

# Metodos e funcoes
# lower / uper / Title (esse ultimo deixa as primeiras letras maiúsculas)
# format
# F-string
# len
# slipt / join
# str.find(char) (retorna index do char) e str.index(char) (se não achar dar erro)
# str.replace(char_to_be_replaced, char_to_replace)

# len
# Por baixo, como tudo em py é objeto, len(str) faz str.__len__ e retorna
password = input("Type your password: ")

if len(password) < 6:
    print("Invalid password")
else:
    print("Valid password")

# OBS: não usar isso para ordenar alfabeticamente duas strings pelo amor de deus
# Falso pois alfabeticamente, o primeiro nome é menor
print("Ana Júlia" > "Vick")

# ljust e rjust -> bota o name em um dos lados e preenche até completar os N chars
name = "Luquetinha"
name.startswith('J')  # mas é só fazer name[0] == 'J'
# Justifica o nome à esquerda e preenche o resto com * ate chegar em 20
nameL = name.ljust(20, '*')
nameR = name.rjust(20, '*')

# INDEXES -> Cada char tem um índex e podemos manipular só o char e afins
# Strings são imutáveis em python, logo não posso fazer str[index] = 'x', tenho qque criar outra

word = "opa meu jovem"
counter = -1  # -1 pois o primeiro char começa com 0 (index 0)

for c in word:
    ++counter
    print(c)
    if c == 'o':
        print(f"Found an O at index {counter}!")

# Extraindo substrings -> str[start:end:step]
size = len(word)
# var[start:end] - é igual a JS, ele não pega o end mas o anterior
subWord = word[0:4]
subWord = word[0:6:3]
# sem não passar nada ele pega daquele ponto até tudo ou a partir do 0 até onde pedi
subWord = word[5:]
subWord = word[:(size - 1)]
print(subWord)
# índices negativos -> o ultimo char sempre começa no -1 e segue

# Split e Join
# Mesma ideia de JS, o split tem um parametro de separação e guarda os itens numa lista
# O join é chamado pelo char que quero que junte e recebe a lista

sentence = "Victoria é muito fofa"
wordList = sentence.split(" ")
print(wordList)

string = "-".join(wordList)
print(string)
