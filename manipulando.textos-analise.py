frase = str(input('Digite a frase:')).strip()
# .strip() serve pra retirar espaços no começo e final

print(len(frase))
# len conta o número de caracteres

print(frase.count('o', 0, 15))
# conta quantas letras o tem e onde começa e termina

print(frase.find('neo'))
# indica local onde está a palavra neo

var = 'carro' in frase
print(var)
# vai dizer se tem ou não carro na variável frase