from abc import *

class Strategy_interface(ABC):

    @abstractmethod
    def pay(self, ammount):
        pass

    @abstractmethod
    def collectPaymentDetails(self):
        pass
