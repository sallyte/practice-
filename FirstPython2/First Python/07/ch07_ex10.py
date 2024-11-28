# for i in range(1,11,1) :
#     print(i)


# total = 0
# for i in range(1,101,1) :
#     total += i
#     print(total)

# 3.1부터 10까지 짝수만 출력

# for i in range(1,11,2) :
#     print(i)

# 4.10부터 1까지 역순으로 출력
# for i in range(10,1,-1) :
#     print(i)

# 5.사용자가 입력한 숫자만큼 반복
# user = int(input('숫자를 입력하세요'))
# for i in range(user) :
#     print(i)

# num = 0
# while num <= 100:
#     if num % 7 == 0:
#         print(num)
    # num -= 1

# for num in range(1,11) :
#     if num % 2 == 0 :
#         break
#     print('num->',num)

# for num in range(1,6) :
#     print(num)
# else :
#     print('반복문이 끝났습니다.')
# x = 2
#  x = int(input('구구단의 단을 입력하세요'))
# for i in range(1,10,1) : 
#     print(x*i)
#     x += 1


# mumbers = [2,3,4,5,6,7,8,9]


# for x in range(2,10):
#     print(f'==={x}단====')
#     for i in range(1,10,1) : 
#         print(f'{x}x{i}={x*i}')
#      # break
#     print(f'{x}단')




mumbers = (2,3,4,5,6,7,8,9)

def printDan(num):
    for i in range(1,10,1):
        print(f'{num}x{i}={num*i}')

for x in mumbers:
    print(f'==={x}단====')

    printDan(x)
    printDan()
   









# loopcnt = 6  #반복 횟수

# for n1 in range(loopCnt) :
#     for n2 in range(loopCnt-n1-1):
#         print(' ', end=' ')

#     for n3 in range((n1+1)*2-1) :
#         print('*',end=' ')

#     print()


# output = " "

#     for i in range(1, 10):
#         for j in range(0, i):
#             output += "*"
#         output += "\n"

# print(output)


# import turtle
# t = tutle.Turtle()
# t.shape('tutle')

# for i in range(1,11):
#     t.corcle(20)
    
#     t.up()
#     t.goto(i*30,0)
#     t.down()


