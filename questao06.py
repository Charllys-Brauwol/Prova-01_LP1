'''6 - Escreva uma função que receba a idade do usuário, se ele for menor pergunte
se ele está acompanhado. Dependendo das respostas indique se ele pode ou não
encher a cara de cachaça.'''

idade = int(input('Vamos saber se você já pode beber.\nQual sua idade?\n'))
acompanhado = int(input('Está acompanhado? (1 - Sim / 2 - Não)\n'))

if (idade >= 18):
    if (acompanhado == 1):
        print ('Parabéns! Você pode beber.')
    else:
        print ('Não pode beber.')
else:
    print ('Não pode beber.')