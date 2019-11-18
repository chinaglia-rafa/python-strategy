class Order:

    def __init__(self):
        self.__isCloded = False
        self.__totalCost = 0

    def processOrder(self, strategy):
        strategy.collectPaymentDetails()

    def setTotalCost(self, value):
        self.__totalCost = value

    def getTotalCost(self):
        return self.__totalCost

    def isClosed(self):
        return self.__isCloded

    def setClosed(self, value):
        self.__isCloded = value
