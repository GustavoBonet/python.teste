nome = str(input('Digite seu nome:')).strip()
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é popular no Brasil!')
elif nome in 'Ana Beatriz Julia':
    print('Um nome muito Bonito!')
else:
    print('Seu nome é estranho!')
