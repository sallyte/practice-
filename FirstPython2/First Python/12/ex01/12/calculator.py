# def add(a,b):
#     return a+b

# def subtract(a,b):
#     return a-b

# def multiply(a,b):
#     return a*b

# def divide(a,b):
#     return a/b

# def rest(a,b):
#     return a%b

def addition(n1, n2, isPrint=False):
    if isPrint == True :
        print('덧셈 연산 결과: ', n1 + n2)
    return n1 + n2
   
def subtraction(n1, n2, isPrint=False):
    if isPrint == True :
        print('뺄셈 연산 결과: ', n1 - n2)
        return n1 - n2

def multiplication(n1, n2, isPrint=False):
    if isPrint == True :    
        print('곱셈 연산 결과: ', n1 * n2)
        return n1 * n2

def division(n1, n2, isPrint=False):
    if isPrint == True :
        print('나눗셈 연산 결과: ', n1 / n2)
    return n1 / n2
   
def rest(n1, n2, isPrint=False):
    if isPrint == True :
        print('나머지 연산 결과: ', n1 % n2)
    return n1 % n2

def portion(n1, n2, isPrint=False):
    if isPrint == True :
        print('몫 연산 결과: ', n1 // n2)
    return n1 // n2

