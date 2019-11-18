from Strategy_interface import Strategy_interface
from CreditCard import CreditCard

class PayByCreditCard(Strategy_interface):

    def __init__(self):
        self.creditCard = None

    def pay(self, ammount):
        if self.creditCard != None:
            print("Pagamento no valor de R$", "{:.2f}".format(ammount), "feito usando Cartão de Crédito!")
            self.creditCard.setAmmount(self.creditCard.getAmmount() - ammount)
            return True
            
        return False

    def collectPaymentDetails(self):
        num = input("Digite o número do cartão: ")
        date = input("Digite a data de experição do cartão mm/yy: ")
        cvv = input("Digite o código de segurança no verso do cartão (CVV): ")
        self.creditCard = CreditCard(num, date, cvv)
