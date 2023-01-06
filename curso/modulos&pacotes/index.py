# NOTE Importando modules

import pathlib  # Importando o modulo todo
from sys import stdin, platform  # Importando partes especificas
import os as system  # Dando alias

print(platform)
print(system.path)

# NOTE o python reconhece todos os modulos em sys.path (onde os modulos sao instalados)
# NOTE Fora do __main__ ele nao reconhece modulos e pacotes
# __main__ é o modulo main, vulgo, o que esta sendo executado em primeiro plano
print("Esse modulo eh o", __name__)

# NOTE __main__ eh o primeiro modulo executado, mas se em um modulo q importei tem um print de __main__
# mas esse print executou pq importei o modulo, o __name__ é o nome do modulo

# NOTE sys.path -> lista de paths que contem modulos e o python procura os imports neles

# NOTE Recarregar módulos -> importlib.reload()
import importlib
importlib.reload(pathlib) # Caso mude algo no modulo e o programa esteja executando
