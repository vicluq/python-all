# NOTE Funcoes Decoradoras -> incrementam e adicionam coisas extra nas funcoes

# Decoradora que recebe a funcao e incrementa funcionalidades
def sum_decorator(sum_func):
    def internal(num1 = 0, num2 = 0):
        num1_cast = num1
        num2_cast = num2
        
        if isinstance(num1, str):
            num1_cast = float(num1)
        elif not num1:
            num1_cast = 0

        if isinstance(num2, str):
            num2_cast = float(num2)
        elif not num2:
            num2_cast = 0
            
        return sum_func(num1_cast, num2_cast)
    
    return internal

# Funcao normal -> sem checagens, conversões, etc. Para nao alterar ela, podemos criar uma decoradora
def sum(num1 = 0, num2 = 0):
    return num1 + num2

decorated_sum = sum_decorator(sum)

print(decorated_sum("2", None))

# NOTE Sintax Sugar dos Decoradores -> uma forma de usar decoradores de forma mais harmoniosa
    # Pode ser para classes ou funcoes
    
@sum_decorator # essa sintaxe passa o elemento logo abaixo para o decorador e ele injeta o comportamento da funcao retornada na nossa
def sum2(num1 = 0, num2 = 0):
    return num1 + num2

print(sum2("2", 3))

# NOTE passando param pro decorator -> @generate_decorator(*args)
    # Quando chamamos um decorator, o python tenta pegar o retorno dele e executar, so que isso é errado
    # Porque eh como se chamassemos 2 vzs, o python uma, pq eh decorator e a gnt chamou dps
    # Logo, o correto eh chamar uma funcao que retorna o decorator pq o python executa o retorno dela (o decorator) ja q nos chamamos ela
    # ! @func_dec -> func_dec retorna a funcao
    # ! @fabrica_dec() -> fabrica_dec retorna o decorator ai o uso fica normal

# NOTE A ordem de aplicacao dos decoradores é de baixo pra cima
    # Aplica uma pegada RECURSIVA
