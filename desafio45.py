import random
numc = [1,2,3]
esc = random.choice(numc)
num = int(input("""Vamos jogar Jokenpo!
Escolha uma das opções:
1 - Pedra
2 - Papel
3 - Tesoura
Escolha informando o número: """))
print('O sistema escolheu: {}'.format(esc))
if num == 1 and esc == 3:
    print('Parabéns você ganhou!')
elif num == 2 and esc == 1:
    print('Parabéns você ganhou!')
elif num == 3 and esc == 2:
    print('Parabéns você ganhou!')
elif num == 1 and esc == 2:
    print('Que pena você perdeu!')
elif num == 2 and esc == 3:
    print('Que pena você perdeu!')
elif num == 3 and esc == 1:
    print('Que pena você perdeu!')
else:
    print('EMPATE!')

