# NOTE Dicionários "{}" -> Nós controlamos o índice (chaves)
    # quando tentamos usar algo de iteráveis com dict, python faz o dict.keys()

# Chaves podem ser numeros, strings, tuplas (tipos de dados imutáveis)
myDict = {'name': 'Victoria', 'age': 20}
print(myDict['name'], myDict['age'])

# Adicionando valores
myDict['college'] = 'UFPE'
print(myDict)

# Se tentarmos acessar uma chave que não existe com os colchetes, recebemos uma exceção
if ('key' in myDict) or (not myDict.get('key') == None):
    print(myDict['key']) # Print se existir

# Values do dicionário (obj.values() em JS) -> é iterável
print('UFPE' in myDict.values())
print(len(myDict)) # Quantos pares de chave/valor

# NOTE Iteração -> por baixo, qnd chamamos o for no dicionario, o python chama o metodo keys para iterar
for key in myDict:
    print(key, '->', myDict[key])

for key in myDict.keys(): # Se fizermos como acima, o python faz isso por baixo
    ...

print(myDict.items()) # Gera um iterável com tuplas (chave, valor)

dictList = list(myDict.items())
print(dictList) # Como recebemos um iterável, posso converter em lista

# NOTE Passagem por referência -> Dicionários são passados por referência, se mudar um, o outro muda pois apontam na mesma memória
    # Para criar uma cópia, faço dict.copy() -> shallow copy, ou sejam algumas coisas podem não surtir efeito
    # module copy -> esse módulo que importamos nos permite fazer uma cópia profunda

# NOTE Métodos
    # keys e values -> retorna uma tupla com as chaves e os values, respectivamente
    # items -> tipo o obj.entries do js
    # dict.copy -> cópia rasa, tudo o que for imutável ele faz a cópia rasa (coisas q não sao por referencia)
    # Pop -> dict.pop(key)
    # del dict[key]
    # dict.get(key) -> se não houver a chave = None

# NOTE Desempacotamento
    # Recebe os values na ordem q foram adicionados

myDict = {"Nome": "vic", "idade": 22}

n, i = myDict.values() # Por baixo -> n, i = myDict.values()
print(n, i)

(k1, val1), (key2, val2) = myDict.items() # (key, value), (key2, value2) = myDict.items() (lembra haskell)

# NOTE extraindo valores do dicionario (Empacotamento)
outroDict = { **myDict, 'outro': 'valor' } # equivale ao ... rest do js