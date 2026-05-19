# 11. Escreva um algoritmo que informe ao usuário que calcula o somatório de uma sequência de números. O algoritmo deverá solicitar ao usuário o total de números que deverão ser somados. Depois o algoritmo deve realizar a soma de todos os números 
# e apresentar na tela o resultado dessa soma conforme exemplo abaixo: 
# Digite o total de números a serem somados: 5 
# 2 7 3 8 6 (números digitados pelo usuário)
# Saída no terminal: 2+7+3+8+6=26

valores = int(input('Qual o total de números que deverão ser somados? '))

soma4 = 0
expressao = ''

for n in range(valores):
    digito = int(input('Digite um valor: '))
    soma4 += digito

    if n == 0:
        expressao += str(digito)
    else:
        expressao += '+' + str(digito)

print(f'{expressao}={soma4}')