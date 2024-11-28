# print("구구단")
# #print("2단 : 2 4 6 8 10 12 14 16 18")


# 2단. x가 2~9사이의 숫자인지 확인하고
# print를 출력.
# 아니면 2~9 사이의 숫자가 아니라고 출력
# x = 2
# if 2 <= x <= 9 :
#      print("2단 :",x*1,x*2,x*3,x*4,x*5,x*6,x*7,x*8,x*9)
# else :
#      print('xsms 2와 9 사이의 숫자가 아닙니다.')

   
# print("2단 :",x*1,x*2,x*3,x*4,x*5,x*6,x*7,x*8,x*9)

# x = 2
# # print(type(x) != int) :

# if(type(x) == int):
#     print('정수를 입력해 주세요') #x가 정수이면 구구단 출력
#     if 2 <= x <= 9 :
#         print("2단 :",x*1,x*2,x*3,x*4,x*5,x*6,x*7,x*8,x*9)
# else :
#     print('정수를 입력하세요.')

# x = 2.0  
# isPrint = True

# if(type(x) != int):
#     isPrint = True
#     print('정수를 입력해 주세요') #x가 정수이면 구구단 출력
    
#     if 2 <= x <= 9 :
#         print("2단 :",x*1,x*2,x*3,x*4,x*5,x*6,x*7,x*8,x*9)
# else :
#     print('정수를 입력하세요.')

# x = 3
# print("3단: 3 6 9 12 15 18 21 24 27")

num = 1
x = int(input('출력할 구구단의 단을 입력하세요'))

while 1 <= num <= 9 :
    print(x * num) 
    num += 1