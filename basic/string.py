### Strings

## Metodos e funcoes
    # lower / uper 
    # format
    # F-string
    # len

# len
password = input("Type your password: ")

if len(password) < 6:
    print("Invalid password")
else:
    print("Valid password")
    
    # OBS: não usar isso para ordenar pelo amor de deus
print("Ana Júlia" > "Vick") # Falso pois alfabeticamente, o primeiro nome é menor

    # Por baixo, como tudo em py é objeto, len(str) faz str.__len__ e retorna