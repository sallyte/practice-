# 함수
# def greet():
#     print('안녕하세요')
#     print('반갑습니다.')
# greet()


# def toTal(a,b):
#     print(a+b)
 
# toTal(10,20)

# a =  [1, 2, 3, 4, 5]
# sum = 0
# for b in a :
#     sum+=b
       
# print('합:',sum)

# a =  [1, 2, 3, 4, 5]
# toTal =sum(a)

# def print_sum(a_number):
#     totalSum = sum(a_number)
#     print(totalSum)
# print_sum(a)

# a =[1, 2, 3, 4, 5]

# def c_sum(a):
#     total =sum(a)
#     print(total)
# c_sum(a)



#짝수인지 출력
# num =2
# if num%2 ==0:
#     print('짝수')

# num = 2

# # if(num % 2 ==0):
# #     print('짝수')
# num = 2
# def print_is_even(number):    
#     if(number % 2 ==0):
#         print('짝수')

# print_is_even(num)



def connectDB():
    print('데이터베이스에 접속한다')

def printMemberInfo():
    getMemberInDB()
    print('회원정보를 출력한다')

def getMemberInDB():
    connectDB()
    selectMemberInDB()
    print('데이터베이스에서 회원정보를 가져온다')

def selectMemberInDB():
    print('데이터베이스에서 회원정보를 검색한다')

printMemberInfo()

# a =[1, 2, 3, 4, 5]
# toTal =sum(a)

# def print_sum(a_number):
#     totalSum =sum(a_number)
#     print(totalSum)
# print_sum(a)



# def print_star():
#     print('********************')

# def print_plus():
#     print('++++++++++++++++++++')

# def print_minus():
#     print('--------------------')



# print_star()
# # print('********************')
# print_plus()
# # print('++++++++++++++++++++')
# print_minus()
# # print('--------------------')