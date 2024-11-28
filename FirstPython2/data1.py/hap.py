class Calculator:
    def add(self, a ,b):
        return a+b
       
class Calculator2:
    def sub(self, a ,b):
        return a-b
    
class Operation:
    def __init__(self, calculator, calculator2 ):
        self.calculator = calculator
        self.calculator2 = calculator2   

    def perform_addition(self , x ,y):
        return self.calculator.add(x, y)
    
    def perform_subtract(self , x ,y):
        return self.calculator2.sub(x, y)
        
    
calculator = Calculator()
calculator2 = Calculator2()
operation = Operation(calculator, calculator2)
result = operation.perform_addition(10, 20)
result2= operation.perform_subtract(10, 20) #필요한 데이터만 전달
print("Addition result:", result)
print("Subtract result:", result2)