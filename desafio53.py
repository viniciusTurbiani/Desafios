frase = str(input('Digite uma frase para ser analisada: '))
frase2 = frase.upper()
len2 = len(frase2)
frase3 =frase2[len2::-1]
print ("The sliced string is:",frase3)
if frase2 == frase3:
    print('A frase digitada é um palindromo!')
else:
    print('A frase digitada não é um palindromo!')