from Strategy_interface import Strategy_interface

class PayByPayPal(Strategy_interface):

    def __init__(self):
        self.email = ''
        self.password = ''
        self.signedIn = False

    def pay(self, ammount):
        if self.signedIn:
            print("Pagamento no valor de R$", "{:.2f}".format(ammount), "feito usando PayPal!")
            return True

        return False

    def collectPaymentDetails(self):
        while not self.signedIn:
            self.email = input("Digite seu e-mail: ")
            self.password = input("Digite a senha: ")
            self.signedIn = self.verify()
            if not self.signedIn:
                print("E-mail ou senha incorretos! Tente a@a.com com senha 123!")

    def verify(self):
        return self.email == 'a@a.com' and self.password == '123'
