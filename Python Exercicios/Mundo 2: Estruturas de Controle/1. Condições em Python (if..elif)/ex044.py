'''
Elabere um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

- a vista dinheiro/cheque: 10% de desconto
- a vista no cartão: 5% de desconto
- em ate 2x no cartao: preço normal
- 3x ou mais no cartao: 20% de juros
'''

produto = float(input())
print("""
1. A vista dinheiro / cartão.
2. A vista no cartão.
3. Em até 2x no cartão.
4. 3x ou mais no cartão.
""")
pagamento = int(input())

if pagamento == 4:
    print('Quantas vezes? ')
    x = int(input())

if pagamento == 1:
    print('Valor a pagar: {:.2f}R$'.format(produto * 0.9))
elif pagamento == 2:
    print('Valor a pagar: {:.2f}R$'.format(produto * 0.95))
elif pagamento == 3:
    print('Valor a pagar: {:.2f}R$'.format(produto))
elif pagamento == 4:
    print('Valor a pagar: {:.2f}R$'.format(produto + (produto/100 * x)))
