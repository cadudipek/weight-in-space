# INPUT INICIAL
pesoterra = float(input('Qual o seu peso na terra? '))

# TABELA PLANETAS
print('=============')
print('DESTINO - PLANETAS')
print('=============')
print('1 - Mercúrio')
print('2 - Vênus')
print('3 - Marte')
print('4 - Júpiter')
print('5 - Saturno')
print('6 - Urano')
print('7 - Netuno')

destino = int(input('Para qual planeta você vai? '))

# CONDIÇÕES
if destino == 1:
    destino = pesoterra * 0.38
    print(f'Peso em Mercúrio: {destino:.2f} kg')

elif destino == 2:
    destino = pesoterra * 0.91
    print(f'Peso em Vênus: {destino:.2f} kg')

elif destino == 3:
    destino = pesoterra * 0.38  # Corrigido o erro de vírgula para ponto
    print(f'Peso em Marte: {destino:.2f} kg')

elif destino == 4:
    destino = pesoterra * 2.53
    print(f'Peso em Júpiter: {destino:.2f} kg')

elif destino == 5:
    destino = pesoterra * 1.07
    print(f'Peso em Saturno: {destino:.2f} kg')

elif destino == 6:
    destino = pesoterra * 0.89
    print(f'Peso em Urano: {destino:.2f} kg')

elif destino == 7:
    destino = pesoterra * 1.14
    print(f'Peso em Netuno: {destino:.2f} kg')

else:
    print('Número do planeta inválido')
