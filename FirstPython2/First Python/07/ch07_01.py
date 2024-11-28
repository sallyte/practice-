# for i in range(100):
#     print('안녕하세요')

# num = 0
# while num < 5 :
#     print(num)
#     num += 2

# num = 1
# while num <= 50 :
#     if num % 3 == 0 :
#         print('3의 배수', num)
#     else:
#         print(f'3의 배수 아님', num)
#     num += 1
# sum = 0
# for num in range(1,11,1) :
#    num += sum
#     print('sum = ', sum)
   

# num = 1
# while 0 <= num < 10 :
#     print(num+1)
#     num += 1

# num = 1
# total = 0
# while  num <= 100 :
#     total += num
#     print(total)
 
# num = 1
# while num <= 10 :
#     if num % 2 == 0 :
#         print('짝수',num)
#     num +=1

# 4. 10부터 1까지 역순 출력

# num = 10
# while 0 < num <= 10 :
#     print(num )
#     num -= 1

# # 5. 사용자가 입력한 숫자만큼 반복
# user = int(input('숫자를 입력하세요.'))
# num = 0

# while num < user :
#     print(num)
#     num  += 1

# count = int(input("숫자를 입력하세요: "))
# i = 0
# while i < count:
#     print(i)
#     i += 1

# import random
# correct_number = random.randint(1,10)

# while True :
#     user = int(input('숫자를 입력하세요'))
#     if user == correct_number:
#         print('정답입니다.')
#         break
#     else :
#       print('틀렸습니다.다시 시도하세요')


# while True :
#     myName = input('이름을 입력해 주세요')
#     myHome = input('사는곳을 입력해 주세요')
#     myMajor = input('전공을 입력해 주세요')
#     break


#     myName = input('이름을 입력해 주세요')
#     myHome = input('사는곳을 입력해 주세요')
#     myMajor = input('전공을 입력해 주세요')

# input('계속하시겠습니까?(계속하려면 엔터,종료하려면 "0"입력):')


while True:
    exit_input =input('계속하시겠습니까?(계속하려면 엔터, 종료하려면 "0"입력)')
    if(exit_input == '0') :
        print('프로그램을 종료합니다.')
        break

    myName = input('이름을 입력해 주세요')
    myHome = input('사는곳을 입력해 주세요')
    myMajor = input('전공을 입력해 주세요')

    print('이름: ', myName)
    print('사는곳: ', myHome)
    print('전공: ', myMajor)


# for i in range(0,8,1) :
#     print(i)

# for i in range(2,80,2):
#     print(i)

# num =int(input('문자발송 횟수'))

# for i in range(1,num+1,1):
#         print('산악회에 초대합니다~',i)


# for i in range(1,100,3):
#     print(i,end=' ')

# for i in range(-10,11,2):
#     print(i)

# for i in range(0,71,5):
#     print(i)

# for i in range(10):
#     print(i,end=' ')

# for i in range(10,0,-1):
#      print(i,end=' ')

# for c in P Y T H O N 
#     print(c)