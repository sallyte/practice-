# class Car: 
#     def __init__(self, model):
#         self.model = model

#     def get_model(self):
#         return self.model
    
# class Driver:
#     def create_car(self, model):
#         return Car (model)
    
# driver = Driver()
# car= driver.create_car("BMW")
# print(f"Driving {car.get_model()}")


# ##의존관계-실체화 관계
# from abc import ABC

# class Vehicle(ABC):
#     def getOn(self):
#         print("Getting on the vehicle.")
#     def getOff(self):
#         print("Getting off the vehicle.")

# class Transferable(ABC):
#     def transfer(self):
#         pass

# class Bus(Vehicle, Transferable):
#     def transfer(self):
#         print("Tranferred to another bus or subway.")

# class Subway(Vehicle, Transferable):
#     def transfer(self):
#         print("Tranferred to another subway or bus.")

# class Taxi(Vehicle):
#       pass

# if __name__ =="__main__":
#     bus = Bus()
#     subway = Subway()
#     taxi = Taxi()
    
#     bus.getOn()
#     subway.getOn()
#     taxi.getOn()

#     bus.getOff()
#     subway.getOff()
#     taxi.getOff()

#     bus.transfer()
#     subway.transfer()

# ###car 파일에서 호출 위한 입력
# # else:
# #     print("Good")

    ##의존관계 역전원칙(위반경우)
# class CreditCard:
#     def make_payment(self):
#         print ("신용카드로 결제했습니다.")
# class DebitCard:
#     def make_payment(self):
#         print ("직불카드로 결제했습니다.")

# class PaymentProcessor:
#     def __init__(self):
#        self.credit_card = CreditCard()
#        self.debit_card = DebitCard()

#     def process_payment(self, a):
#       if a == "credit": 
#         self.credit_card.make_payment() 
#       elif a == "debit": 
#         self.debit_card.make_payment() 
#       else: 
#         print("알 수 없는 결제 수단입니다.")

# if __name__ =="__main__":
#     payment_processor =PaymentProcessor()
#     payment_processor.process_payment(self, a)


##의존관계 역전원칙(준수 경우)

# from abc import ABC, abstractmethod

# class PaymentMethod(ABC):
#     @abstractmethod
#     def make_payment(self):
#         pass

# class CreditCard(PaymentMethod):
#     def make_payment(self):
#         print("신용카드로 결제했습니다.")

# class DebitCard(PaymentMethod):
#     def make_payment(self):
#         print("직불카드로 결제했습니다.")

# class PaymentProcessor:
#     def __init__(self, payment_method: PaymentMethod):
#         self.payment_method = payment_method
#     def process_payment(self):
#         self.payment_method.make_payment()

# if __name__ == "__main__":
#     credit_card = CreditCard()
#     payment_processor = PaymentProcessor(credit_card)
#     payment_processor.process_payment()

#     debit_card = DebitCard()
#     payment_processor = PaymentProcessor(debit_card)
#     payment_processor.process_payment()


##의존성 주입(세터주입)

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self):
        pass

class CreditCard(PaymentMethod):
    def make_payment(self):
        print("신용카드로 결제했습니다.")

class DebitCard(PaymentMethod):
    def make_payment(self):
        print("직불카드로 결제했습니다.")

class PaymentProcessor:
    def __init__(self):
        self.payment_method = None

    def set_payment_method(self,payment_method:PaymentMethod):
        self.payment_method = payment_method

    def process_payment(self):
        if self.payment_method:
            self.payment_method.make_payment()
        else:
            print("결제 수단이 설정되지 않았습니다.")
      
credit_card = CreditCard()
payment_processor = PaymentProcessor()
payment_processor.set_payment_method(credit_card)
payment_processor.process_payment()
