# crescente
n = 0
while n < 100:
    n += 1
    print(n)

# decrescente
n = 100
while n > 1:
    n -= 1
    print(n)

# Escreva um algoritmo que solicite ao usuário dois valores para determinação de um intervalo. Ao final o algoritmo deverá imprimir todos os números desse intervalo e o somatório deles.
a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))

soma = 0

for n in range(a,b+1):
    soma += n
    print(n)

print(f'A soma do intervalo entre os números é: {soma}')

# Escreva um algoritmo que solicite do usuário 10 números e ao final imprima na tela o somatório desses números.

soma2 = 0

for n in range (10):
    numero = int(input('Digite um número: '))
    soma2 += numero

print(f'Somatório dos números: {soma2}')

# 5. Escreva um algoritmo que solicite do usuário 5 valores e ao final apresente na tela o somatório dos valores menores que 10.

soma3 = 0

for n in range(5):
    valores = int(input('Digite um valor: '))
    if valores < 10:
        soma3 += valores

print(f'As somas dos nºs menores que 10 são: {soma3}')

# Escreva um algoritmo que solicite do usuário 5 valores e ao final apresente na tela o somatório dos valores maiores ou igual a 10 e menor do que 20.

soma4 = 0

for n in range(5):
    valores2 = int(input('Digite um valor: '))
    if 10 <= valores2 < 20:
        soma4 += valores2

print(f'Somatório: {soma4}')

# 7. Escreva um algoritmo que solicite do usuário 5 valores e afinal apresente na tela o somatório dos valores pares que foram digitados.
soma5 = 0

for n in range(5):
    valor3 = int(input('Digite um valor: '))
    if valor3 % 2 == 0:
        soma5 += valor3

print(f'A soma dos pares é: {soma5}')

# 8. Escreva um algoritmo que solicite do usuário um número correspondente à quantidade de valores que o usuário fornecerá para o algoritmo. Ao final, o algoritmo deverá informar quantos números pares foram digitados.
pergunta_valor = int(input('Quantas vezes você quer rodar? '))

npares = 0

for n in range (pergunta_valor):
    valor = int(input('Digite um número: '))

    if valor % 2 == 0:
        npares += 1

print(f'Números pares digitados: {npares}')

# 9. Escreva um algoritmo que solicite do usuário 10 valores. O algoritmo deverá calcular a soma da sequência de valores pares e dos valores ímpares, ou seja, somar o 1o número digitado com o 3o, 5o, 7o e 9o e o mesmo para os números pares. Após, informar se o somatório dos números ímpares é maior, igual ou menor do que o dos números pares.

pares = 0
impares = 0

for n in range(10):
    valores = int(input('Digite um valor: '))
    if valores % 2 == 0:
        pares += valores
    else:
        impares += valores

print(f'A soma dos pares são: {pares}')
print(f'A soma dos ímpares são: {impares}')

# 10. Escreva um algoritmo que solicite do usuário 10 valores inteiros. O algoritmo deverá calcular o somatório dos números pares e dos números ímpares que forem digitados pelo usuário. 
# Após o somatório, o algoritmo deve informar se o somatório dos números ímpares é maior, igual ou menor do que o dos números pares.

soma_pares = 0
soma_impares = 0

for n in range(10):
    val_inteiros = int(input('Digite um valor inteiro: '))

    if val_inteiros % 2 == 0:
        soma_pares += val_inteiros
    
    else:
        soma_impares += val_inteiros
    
if soma_pares > soma_impares:
    print(f'A soma dos ímpares é menor que a dos pares')
elif soma_pares == soma_impares:
    print(f'A soma dos ímpares é i igual a dos pares')
else:
    print(f'A soma dos ímpares é maior que a dos pares')

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