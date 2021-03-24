'''10 - Escreva um programa que gere automaticamente uma lista com 100 inteiros e
faça o que se pede a seguir:
● Uma lista com os números pares
● uma lista com os números múltiplos de 5'''

lista = []
for i in range(1, 101):
    lista.append(i)
print('Lista:')
print(lista)

lista_02 = [numero for numero in range(1, 101) if numero % 2 == 0]
print('Números pares:')
print(lista_02)

lista_03 = [numero for numero in range(1, 101) if numero % 5 == 0]
print('Multiplos de 5:')
print(lista_03)