import re
import numpy as np

cpf = '465.684.332-68'

#
# 1º passo
#
def validarCPF(cpf: str):
    # Transformar em números inteiros:
    digitos = re.sub("[^0-9]", "", cpf)
    digitos_np = np.array([int(i) for i in digitos])
    
    # Criar os multiplicadores:
    multiplicador_1 = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2])
    multiplicador_2 = np.array([11, 10, 9, 8, 7, 6, 5, 4, 3, 2])

    # Pegar os 9 primeiros dígitos do CPF,
    # Multiplicar pelos números de 2 a 10 em ordem descrecente,
    # Multiplicar o resultado da soma por 10 e dividir por 11:
    primeiro_digito_valido = sum(digitos_np[0:9] * 10 * multiplicador_1) % 11

    # Pegar os 10 primeiros números,
    # Multiplicar pelos números de 11 a 2 em ordem descrecente,
    # Multiplicar o resultado da soma por 10 e dividir por 11:
    segundo_digito_valido = sum(digitos_np[0:10] * 10 * multiplicador_2) % 11

    # Se o resto da divisão bater com o primeiro dígito, temos o primeiro ponto de validez e...
    # se o resto da divisão bater com o segundo dígito, temos o segundo ponto de validez
    if digitos_np[9] == primeiro_digito_valido and digitos_np[10] == segundo_digito_valido:
        print(f'O CPF {cpf} é válido')
    else:
        print(f'O CPF {cpf} é inválido')


validarCPF(cpf)