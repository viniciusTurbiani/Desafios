print("""========== Banco CEV ==========
   Quanto voce deseja sacar?   
===============================""")
valor = int(input('Informe o valor que será sacado: '))
c50 = valor // 50
c20 = (valor%50)//20
c10 = ((valor%50)//20)//10
c1 = (valor%10)//1
print(f'cedulas de 50: {c50}')
print(f'cedulas de 20: {c20}')
print(f'cedulas de 10: {c10}')
print(f'cedulas de 1: {c1}')