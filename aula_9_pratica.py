print("""A alfabetização é uma fase primordial 
no desenvolvimento das crianças. 
Para isso, é preciso ser o mais didático possível 
no processo de aprendizagem de leitura e 
interpretação dos pequenos.""")
frase = 'Curso em Video Python'
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
frase.replace('Python','Android')
print(frase)
frase = frase.replace('Python','Android')
print(frase)
print(frase.find('video'))
print(frase.lower().find('video'))
frase = 'Curso em Video Python'
dividido = frase.split()
print(dividido[2]) #traz a palavra na posição dois da lista criada a partir da frase
print(dividido[2][3]) #traz o caracetre da palavra da lista