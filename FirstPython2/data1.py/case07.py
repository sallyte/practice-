
##집합관계
class Case:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"Case(Brand:{self.brand}, Model: {self.model} )"
    
class Monitor:
    def __init__(self, brand, size):
        self.brand =brand
        self.size = size

    def __str__(self):
        return f"Monnitor(Brand: {self.brand}, Size: {self.size} inches)"
    

class Keyboard:
    def __init__(self, brand, is_mechanical):
        self.brand = brand
        self.is_mechanical = is_mechanical
    def __str__(self):
        return f"Keboard(Brand: {self.brand}, Mechanical: {self.is_mechanical})"

class Graphic:
     def __init__(self, brand, is_dedicated): 
                    self.brand = brand 
                    self.is_dedicated = is_dedicated  
     def __str__(self):
        return f"Keboard(Brand: {self.brand}, Mechanical: {self.is_dedicated})"

class Computer:
    def __init__(self,case,monitor, keyboard,graphic ):
        self.case = case            # Case 객체
        self.monitor = monitor      # Monitor 객체
        self.keyboard =keyboard     # Keyboard 객체
        self.graphic =graphic

    def __str__(self):
        return (f"Computer\n"
                f"  {self.case}\n"
                f"  {self.monitor}\n"
                f"  {self.keyboard}\n" 
                f"  {self.graphic}")
  #각 구성 요소의 인스턴스 생성  
case = Case("Cooler Master", "H500")
monitor = Monitor("Dell", 27)
keyboard = Keyboard("Logitech", True)
graphic = Graphic("Nvidia", True)
#컴퓨터 인스턴스 생성
computer =Computer(case, monitor, keyboard, graphic)
#컴퓨터 구성요소 출력
print(computer)


##합성관계

class Case:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"Case(Brand:{self.brand}, Model: {self.model} )"
    
class Monitor:
    def __init__(self, brand, size):
        self.brand =brand
        self.size = size   #인치단위

    def __str__(self):
        return f"Monnitor(Brand: {self.brand}, Size: {self.size} inches)"
    
class Keyboard:
    def __init__(self, brand, is_mechanical):
        self.brand = brand
        self.is_mechanical = is_mechanical   #True면 기계식 키보드
    def __str__(self):
        return f"Keboard(Brand: {self.brand}, Mechanical: {self.is_mechanical})"

class Laptop:
    def __init__(self, brand):
        self.case = Case(brand, "ZenBook Pro")
        self.monitor = Monitor(brand, 15.6)
        self.keyboard = Keyboard(brand, True)

    def __str__(self):
        return (f"Laptop\n"
                f"  {self.case}\n"
                f"  {self.monitor}\n"
                f"  {self.keyboard}") 
    
 #Laptoop 인스턴스 생성       
laptop = Laptop("ASUS")
 #Laptoop 구성요소 출력 
print(laptop)
                
        
    
