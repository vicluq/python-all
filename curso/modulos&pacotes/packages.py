# NOTE São pastas de módulos -> podemos criar packages e importar modulos de pastas

# NOTE O Import -> vamos usando a notacao ponto para acessar os modulos dentro dos packages
import package.utils as utils
import package.subpackage.teste as teste

print(utils.concatStrings("Victoria", "Luquet"))

# NOTE __all__ -> é uma lista do que o módulo exporta. se usarmos __all__, ele so exporta oq ta la 

# NOTE Importar modulo dentro de modulo importado
    # Devemos ter cuidado pois, o modulo __main__ que chama o modulo é o contexto, ent se eu importar modulo detro do modulo importado
    # pode dar problema, pois, o contexto eh o __main__ ent ele busca modulos de qlqr arquivo no contexto da main
    # Pra flexibilizar quando importamos modulos dentro de modulos:
        # ao inves de package.modulo -> .modulo, pois o . simboliza referencia a pasta/contexto atual
        # Logo, se meu main ta no diretorio atual e importo um modulo q ta num package e esse modulo importa outro do package, uso o . pra dizer q ta pegando do diretorio em relacao ao modulo que o importou e nao nomeio o package pra n dar conflito

# NOTE __init__.py -> é como se fosse o index.js, sempre que importo algo de um package, esse arquivo é executado, logo posso "exportar" coisa por ele tb
    # Posso importar tudo dos modulos dos packages nele -> import .modulo
    