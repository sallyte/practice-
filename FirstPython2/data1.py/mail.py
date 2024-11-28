
##<스탬프 결합>

class User:
    def __init__ (self, username, email, phone):
        self.username = username
        self.email = email
        self.phone = phone

class EmailSender:
    def send_email(self, user):
        print(f"Sending email to{user.email}")

class NotificationService:
    def __init__(self, email_sender):
        self.email_sender = email_sender

    def notify(self, user):
        self.email_sender.send_email(user)

# 실행
user = User("johndoe","john@example.com","123-456-7890")
# a = input("이름을 입력하세요")
# b = input("메일을 입력하세요")
# c = input("연락처를 입력하세요")
# user = User(a,b,c)

email_sender = EmailSender()
notification = NotificationService(email_sender)

notification.notify(user)
       
##<제어결합>
class Sorter:
    def sort_data(self ,data, sort_type):
        if sort_type == 'asc':
            return sorted(data)
        elif sort_type == 'desc':
            return sorted(data, reverse = True)
class DataProcessor:
    def __init__(self, sorter):
        self.sorter = sorter

    def process(self, data, sort_type):
        return self.sorter.sort_data(data, sort_type)
    
sorter = Sorter()
processor = DataProcessor(sorter)
sorted_data = processor.process([5,2,9,1], 'asc')
print("Sorted data:", sorted_data)
      

##<외부결합>
class PaymentGateway:
    def process_payment(self, amount):
        print(f"Processing payment of {amount} through exernal gateway.")

class OrderProcessor:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def checkout(self, amount):
        self.payment_gateway.process_payment(amount)

gateway = PaymentGateway()
processor = OrderProcessor(gateway)
processor.checkout(100)


##<공통 결합>
#전역변수
shared_data = []

class ModuleA:
    def add_data(self, data):
        global shared_data
        shared_data.append(data)

class ModuleB:
    def print_data(self):
        global shared_data
        print(shared_data)

module_a = ModuleA()
module_a.add_data("Hello")

module_b = ModuleB()
module_b.print_data() 