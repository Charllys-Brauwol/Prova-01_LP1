'''8 - Faça uma função que receba duas listas e que gere uma terceira com itens
únicos'''


lista_01 = [1, 2, 2, 4]
lista_02 = [5, 7, 7, 8]

def unir(lista_01, lista_02):
    lista_03 = list(set(lista_01+lista_02))
    return lista_03

print(unir(lista_01, lista_02))

