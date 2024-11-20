frase = 'Curso em Video Python'
#fatiamento
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
#analise
print(len(frase)) #tamanho
print(frase.count('o')) #conta qtd letras ou palavras
print(frase.count('o',0,13)) #conta qtd letras mais fatiamento
print(frase.find('deo')) #momento onde começa a frase especificada
print(frase.find('Android')) #momento onde começa a frase especificada
print('Curso' in frase) # existe a palavra na variavel
#transformação
print(frase.replace('Python','Android')) #troca lugar
print(frase.upper()) #deixa maiusculo
print(frase.lower()) #deixa minusculo
print(frase.capitalize()) #só a primeira maiuscula
print(frase.title()) #primeira de cada palavra maiuscula
frase = '   Aprenda Python  '
print(frase.strip()) #remove espaços desnecessários do inicio e fim da palavra
print(frase.rstrip()) #remove espaços desnecessários do fim da palavra
print(frase.lstrip()) #remove espaços desnecessários do inicio da palavra
#divisão
frase = 'Curso em Video Python'
print(frase.split())
#junção
print('-'.join(frase))