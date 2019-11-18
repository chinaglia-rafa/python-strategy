from PayByPayPal import PayByPayPal
from PayByCreditCard import PayByCreditCard
from Order import Order

opt = -1

prices = [4.00, 5.00, 75.00]

total = 0

order = Order()
strategy = None

while 1 > opt or opt > 3:
    print("\nBem vindo. Digite uma opção: (Total R$ " + ("{:.2f}".format(total)) + ")\n")
    print("     1 - Refrigerante 35ml")
    print("     2 - Cerveja 1L")
    print("     3 - Tequila Mexicana Kali'ente")
    opt = int(input("/> "))

    if 1 > opt or opt > 3:
        continue

    count = int(input("Quantidade: "));

    total += prices[opt - 1] * count

    if (input("Deseja adicionar outro produto? [s/n] ") == "s"):
        opt = -1

opt = -1
while 1 > opt or opt > 2:
    print("Escolha um método de pagamento: \n")
    print(" 1 - PayPal")
    print(" 2 - Cartão de Crédito")
    opt = int(input("/> "))

if opt == 1:
    strategy = PayByPayPal()
else:
    strategy = PayByCreditCard()

order.setTotalCost(total)

print("Iniciando pagamento")

order.processOrder(strategy)

print("Executando pagamento")
if strategy.pay(order.getTotalCost()):
    print("Pagamento concluído com sucesso!")
else:
    print("Algo saiu errado! Tente novamente mais tarde.")

order.setClosed(True)
