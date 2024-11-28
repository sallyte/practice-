
# def connectDB():
#     print('데이터베이스에 접속한다')

# def printMemberInfo():
#     getMemberInDB()
#     print('회원정보를 출력한다')

# def getMemberInDB():
#     connectDB()
#     selectMemberInDB()
#     print('데이터베이스에서 회원정보를 가져온다')

# def selectMemberInDB():
#     print('데이터베이스에서 회원정보를 검색한다')

# printMemberInfo()


# def introKor():
#     print('안녕.')

# def introEng():
#     print('Hello.')

# def introJap():
#     print('こんにちは.')

# selectNum = int(input('where are you from? 1.한국, 2.USA, 3.Japan'))

# if(selectNum == 1):
#     introKor()
# elif(selectNum == 2):
#     introEng()
# elif(selectNum == 3):
#     introJap()
# else:
#     introEng()



# mumbers = [2,3,4,5,6,7,8,9]


# for x in range(2,10):
#     print(f'==={x}단====')
#     for i in range(1,10,1) : 
#         print(f'{x}x{i}={x*i}')
#      # break
#     print(f'{x}단')




# mumbers = (2,3,4,5,6,7,8,9)

# def printDan(num):
#     for i in range(1,10,1):
#         print(f'{num}x{i}={num*i}')

# for x in mumbers:
#     print(f'==={x}단====')

#     printDan(x)
   


# def print_star():
    # print('********************')

# def print_plus():
#     print('++++++++++++++++++++')

# def print_minus():
#     print('--------------------')


# print('*' * 20)

# def print_symbol(symbol,num):
#     for a in range(num):
#         print(symbol, end='')
# print()


# for a in range(20):
#     print('+', end='')
# print()

# for a in range(20):
#     print('-', end='')
# print()

# print_symbol('*',20)
# # print('********************')
# print_symbol('-',20)
# # # print('++++++++++++++++++++')
# print_symbol('+',20)
# # print('--------------------')

'---------------------------------------------------------'

#def print_star(symbol, num) :
def print_symbol(symbol, num) :
    #print('********************')
    #print('*' * 20)
    
    for i in range(num):
        print(symbol, end='')
    print()

'''
def print_plus(num) :
    #print('++++++++++++++++++++')
    
    for i in range(num):
        print('+', end='')
    print()

def print_minus(num) :
    #print('--------------------')
    
    for i in range(num):
        print('-', end='')
    print()
'''

print_symbol('*', 20)
#print('********************')
#print_plus(20)
print_symbol('-', 20)
#print('++++++++++++++++++++')
print_symbol('+', 20)
#print('--------------------')
print_symbol('*', 20)
#print('********************')
print_symbol('-', 20)
#print('++++++++++++++++++++')
print_symbol('+', 20)
#print('--------------------')
print_symbol('*', 20)
#print('********************')
print_symbol('-', 20)
#print('++++++++++++++++++++')
print_symbol('+', 20)
#print('--------------------')

def put(symbol,num):
    for i in range(num):
        print(symbol, end='')
    print()          #다음줄 넘기기
put('*',20)
put('+',20)
put('-',20)