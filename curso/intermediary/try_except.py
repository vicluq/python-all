# NOTE Try / Except -> ao inves de parar a execucao do cod, nos permite tratar o BO e seguir
    # * No geral, excecoes são classes em python

try: # Tenta executar o codigo e caso ache uma excecao, pula pro bloco do except
    a = 10
    b = 0
    c = a / b # divisao por 0 gera uma excecao
    print("Nao chega aqui, vai pro except na linha acima")
except:
    # ! tratamos o erro
    print("Dividir por 0 é paia, ta?")
    
print("Cod segue normal pois capturamos e tratamos o erro")

# NOTE Capturando excecoes especificas
try: # Tenta executar o codigo e caso ache uma excecao, pula pro bloco do except
    a = 10
    b = 0
    c = a / b # divisao por 0 gera uma excecao
    print("Nao chega aqui, vai pro except na linha acima")
except ZeroDivisionError: # ? Capturando apenas a div por 0, o resto para a exec do cod
    print("Dividir por 0 é paia, ta?")
except (TypeError, IndexError) as error: # ? Conjugando dois erros + capturando a mensagem de erro
    print("Erro de tipo e erro de indexacao")
    print(f"msg: {error}\nname: {error.__class__.__name__}")
except:
    print("Qualquer outro erro")
finally:
    # sempre sera executado no fim de tudo, mesmo que ocorra um erro
    ...
    
# NOTE Gerando Erros - raise ErrorClass(msg)
def createRequestResponse(statusCode, msg):
    if(statusCode < 200 or statusCode > 600):
        raise ValueError("Status code is out of bounds") # Gera uma excecao e para o codigo
    if not msg:
        raise Exception("Mensagem invalida ou vazia") # Gerando uma excecao sem classe especifica
    
    return { 'status': statusCode, 'msg': msg }

