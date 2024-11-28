# count =1

# def addCount():
#     print('count',count)

# print('count',count)
# addCount()


# count =1

# def addCount():
#     count = 2
#     print('count',count)

# print('count',count)
# addCount()


# count =1

# def addCount():
#     global count
#     count = 2
#     print('2.count',count)

# print('1.count',count)
# addCount()
# print('3.count',count)


# def findMax(*nums):
#     print(type(nums))

#     max = 0
#     for n in nums:
#         if n> max:
#             max = n
#     print('최대값:',max)

# findMax(10,20,30)
# findMax(10,20,30,40)
# findMax(10,20,30,40,50)
# findMax(10,20,30,40,50,60)



# def introduce(name, age, addr):
#     print('안녕하세요 저는',name, '이고,' , age,'살 이며,사는곳은',addr,'입니다.')

# introduce('박성래','서울 은평구', 22)
# introduce(name= '이지훈', addr= '서울 동작구', age=43)

# def add(n1,n2,n3):
#     sum = n1+n2+n3
#     return sum
# result = add(1,2,3)
# print(result)

# def add(n1,n2,n3):
#   print(n1+n2+n3)
    
# add(1,2,3)

# def star():
#   print('a')
#   print('b')
#   print('c')
#   return
#   print('a')
#   print('a')
# star()

# def calculator(num1,num2):
#   result1

##p,373
# str = input('영어 단어를 입력하세요')

# eng = {'apple':'사과','chair':'의자', 
#         'doll':'인형', 'book':'책',
#         'piano':'피아노','clock':'시계'}

# val = eng['apple']

# def a(put)
#     return eng[str]

# print(apple)



str = input('영어 단어를 입력하세요')

# def a(apple):
#     return eng[apple]

eng = {'apple':'사과','chair':'의자', 
        'doll':'인형', 'book':'책',
        'piano':'피아노','clock':'시계'}
val = eng['apple']

print(str,val)

# # apple = 사과
# # chair = 의자
# # doll = 인형
# # book = 책
# # piano = 피아노
# # clock = 시계

# 재귀함수 정의
# def fatorialFun(num):
#   if num == 1:
#      return 1
#   else:
#     return num * fatorialFun(num - 1)  #재귀함수 호출

# inputData = int(input('0보다 큰 숫자를 입력하세요.'))
# result = fatorialFun(inputData)
# print(inputData,'팩토리얼은',result,'입니다.')