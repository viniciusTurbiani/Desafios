valorc = float(input('Informe o valor total do imovel: '))
valors = float(input('Informe o valor do salário: '))
anos = int(input('Informe em quantos anos será pago: '))
mensalidade = (valorc//anos)//12
print(mensalidade)
if mensalidade > (valors*0.3):
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')
