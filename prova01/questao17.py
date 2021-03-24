'''17 - Escreva três funções sendo que: 
A Primeira deve receber uma distância em KM e retornar o equivalente em metros.
A segunda deve receber a distância retornada pela primeira função 
e retornar o equivalente em centímetros
A terceira por sua vez recebe a quantidade de centímetros da segunda e retorna o
equivalente em milímetros. 
Utilize as funções como parâmetros.'''

km = int(input('Quantos Km´s você quer converter em metros?\n'))

def km_metros(km):
    return (km * 1000)

print (f'{km} km(s) são {km_metros(km)} metro(s).')

def metros_centimetros(km_metros):
    return (km_metros(km) * 100)

print (f'{km_metros(km)} metro(s) são {metros_centimetros(km_metros)} cm(s).')

def cm_ml(metros_centimetros):
    return (metros_centimetros(km_metros) * 10)

print (f'{metros_centimetros(km_metros)} cm(s) são {cm_ml(metros_centimetros)} ml(s).')