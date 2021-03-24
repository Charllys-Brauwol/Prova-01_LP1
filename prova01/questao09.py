'''9 - Um fazendeiro cria Galinhas, Vacas e Porcos, Cavalos, Girafas, sim ele é um
fazendeiro ousado. Escreva uma função que receba a quantidade de cada animal
que o fazendeiro possui atualmente e retorne quantas patas tem na fazenda.'''

galinha = int(input('Quantas galinhas você têm?'))
vaca = int(input('Quantas vacas você têm?'))
porco = int(input('Quantas porcos você têm?'))
cavalo = int(input('Quantas cavalos você têm?'))
girafa = int(input('Quantas girafas você têm?'))

def patas(galinha, vaca, porco, cavalo, girafa):
    total = ((galinha * 2) + ((vaca + porco + cavalo + girafa) * 4))
    return total

print(f'O total de patas é:\n{patas(galinha, vaca, porco, cavalo, girafa)}')