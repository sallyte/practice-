class Calculator:    #클래스 선언
    #  num1 = 0
    #  num2 = 0
    def __init__(self, n1, n2):    #속성
        self.num1 = n1
        self.num2 = n2

    def addition(self, isPrint=False):
        if isPrint == True :
             print('덧셈 연산 결과: ', self.num1 + self.num2)
        return self.num1 + self.num2
   
    # def add(self):                 #메서드 정의
    #     print('add')
    #     return self.num1 + self.num2
    
calc = Calculator(10,20)   # calc 객체 선언 및 초기화
print(type(calc))
calc.addition(True)

print(calc.num1)
print(calc.num2)


calc2 = Calculator(1,2)  # calc2 객체 선언 및 초기화
calc2.addition(True)