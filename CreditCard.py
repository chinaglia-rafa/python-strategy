class CreditCard:

    def __init__(self, number, date, cvv):
        self.__ammount = 500
        self.__number = number
        self.__date = date
        self.__cvv = cvv

    def setAmmount(self, ammount):
        self.__ammount = ammount

    def getAmmount(self):
        return self.__ammount
