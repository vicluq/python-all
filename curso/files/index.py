caminho_na_pasta_atual = "file.txt" # Caminho na pasta q eu to, só passo o nome
caminho_geral = "/Users/victorialuquet/Desktop/test.txt" # pwd para saber o diretório

# NOTE Modos de Abertura
# r (leitura, deve existir ele), w (escrita, apaga oq ja tiver), x (exclusivamente criacao)
# a (append), b (binário), t (texto + leitura e escrita)
# ! Os modos de escrita criam também, mas o x APENAS cria
# ? Botando o "+" depois de uma das letras, ele abre no modo extendido
# ex: se for r+ (ler e escreve), etc

# NOTE Context Manager 
# with (abre e fecha)

# NOTE Métodos Úteis
# write, read
# writelines (escreve várias linhas)
    # * passamos um iteravel e ele escreve cada elemento do iterável
# seek (move o cursor no arquivo)
    # * A cada operacao que que fazemos (leitura ou escrita), o cursor do mouse vai para a prox linha (obs msm assim nos devemos da quebra de linha nos textos)
    # * por isso, o seek pode ser util para mover entre linhas
# readline
# readlines

# NOTE Apagar, renomear

# os.remove ou os.unlink -> passa o path e ele remove do sistema
# os.rename

# ! OBS: lembrar de sempre fechar o arquivo


my_file = open(caminho_na_pasta_atual, 'r')
my_file.close()

with open(caminho_na_pasta_atual, 'a+') as my_file:
    ... # esse código faz a mesma coisa do open/close mas em um escopo próprio
    print("Fechando arquivo...")
    
