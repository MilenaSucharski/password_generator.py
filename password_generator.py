import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

print("=== GERADOR DE SENHAS ===")

tamanho = int(input("digite o tamanho da senha: "))

senha = gerar_senha(tamanho)

print("senha gerada:", senha)
