# Ambientes Virtuais

- Servem para utilizarmos como um ambiente de desenvolvimento
- Podemos criar um ambiente para cada instncia do projeto uma vez q nos permite instalar versoes específicas
- Biblioteca nativa: **venv**

## Como Funciona

- Ao criar um venv em um diretório, toda a instalacao do python é instalada nesse diretório
- Sempre que eu instalar algo no venv, fica so no venv, e isso é mais uma vantagem (fica na pasta lib)

## Criando um venv

- Criar um novo projeto
- Detalhe, ela **NÃO** vai para o git pois fica grande **(tipo a node_modules)**
- No terminal no diretório do projeto, digitar:

```bash
    python -m venv "nome do ambiente"
```

OBS: _-m_ é a flag para executar uma lib (nesse caso a venv), ou seja, os scripts dela

- No diretório que ta a venv, para ativar só rodar: `source | . venv/bin/activate`
- Para parar de rodar: `deactivate`
- Para saber qual é o python usado: `wich`

OBS: Quando o ambiente de um projeto ta inativo, ele usa o python do diretório de instalacao na máquina, porém quando o ambiente ta ativo e a gnt quer ver qual python o projeto usa, ele agora mira no do amiente (na pasta do ambiente). Ouseja, o pip, etc, tudo vai ser do ambiente quando ele ta ativo. 

- Ao instalar bibliotecas, elas serão instaladas pelo pip do venv e não ficarão no python do sistema (global)

## Instalando Pacotes

```bash
    python -m pip install [package] # Quando a segunda da erro essa eh bem
    pip install [package]
    pip install [package] --upgrade # update de pacote

    # Desinstalando
    pip uninstall [package]

    # Listar versoes de um pacote
    pip index versions [package]
    pip install[package]==versao

    # Listar pacotes instalados no venv e suas versoes
    pip freeze

    # Gerando o requirements.txt para o venv (libs que ele precisa)
    pip freeze > requirements.txt

    # Instalando os pacotes do arquivo
    pip install -r ./requirements.txt
```