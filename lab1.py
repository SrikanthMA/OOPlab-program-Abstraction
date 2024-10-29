from abc import ABC,abstractmethod
class Bank(ABC):
    def bank_info(self):
        print("Welcome to the Bank")

    @abstractmethod
    def interest(self):
        "Abstract method"
class SBI(Bank):
    def interest(self):
        "Implement of the abstract method"
        print("In SBI 5% interest")
s=SBI()
s.bank_info()
s.interest()        
