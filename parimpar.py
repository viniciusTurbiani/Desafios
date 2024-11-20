import random
v = 0
soma = 0
while v == 0:
    print('-----VAMOS JOGAR PAR OU IMPAR!-----')
    p = str(input('Voce quer par ou impar? [P] ou [I]: '))
    n = int(input('Informe um número para jogar: '))
    c = random.randint(0,10)
    r = (n+c)%2
    if r > 0 and p == 'I':
        v = 0
        soma = soma + 1
        print('Você venceu!')
    else:
        v = 1
        print('VocÊ perdeu!')
print(f'Você teve {soma} vitorias')