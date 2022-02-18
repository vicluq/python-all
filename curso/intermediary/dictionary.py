# NOTE Dicionários "{}" -> Nós controlamos o índice (chaves)

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

# Iteração
for key in myDict:
    print(key, '->', myDict[key])

print(myDict.items()) # Gera um iterável com tuplas (chave, valor)

dictList = list(myDict.items())
print(dictList) # Como recebemos um iterável, posso converter em lista

# Passagem por referência -> Dicionários são passados por referência, se mudar um, o outro muda pois apontam na mesma memória
    # Para criar uma cópia, faço dict.copy() -> shallow copy, ou sejam algumas coisas podem não surtir efeito
    # module copy -> esse módulo que importamos nos permite fazer uma cópia profunda

# Pop -> dict.pop(key)