# dollar = 1167
# # 엔 = 1.096
# # 유로 = 1268
# # 위안 =171

# total = float(input('입력 : '))
# print( total * dollar,'원')


# import operator

n1 = float(input('첫 번째 숫자를 입력하세요: '))
n2 = float(input('두 번째 숫자를 입력하세요: '))
op = input('연산자를 입력하세요(+,-,*,/):')
# # print(type(op))

# def sum(a,b):
#     if type(a) != float:
#         print('실수가 아닙니다.')
#         return -1
#     if type(b) != float:
#         print('실수가 아닙니다.')
#         return -1
#     return a+b
import calculator as ca

if op == '+' : 
    result = ca.addition(n1,n2)
    # print(num1+num2)
elif op =='-' : 
    result = ca.subtraction(n1,n2)

elif op == '*' : 
    result = ca.multiplication(n1,n2)

elif op == '/' :     
    result = ca.division(n1,n2)

elif op == '%' :     
    result = ca.rest(n1,n2)

else :
    print('연산자를 입력해 주세요')
print(result)

# def sum(a,b):
#     add = num1+num2
#     if op == '+' : 
# #     print(num1+num2)
# sum ()  


# def addFuntion(num):
#     if num > 0:
#         print('num:',num)
#         addFuntion(num - 1)
# addFuntion(10)