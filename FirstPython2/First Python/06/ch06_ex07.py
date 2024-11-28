score = int(input('점수를 입력하세요'))

if score >= 90:
    print('A')
elif score >= 80:
     print('B')
elif score >= 70:
     print('C')
elif score >= 60:
     print('D')
else:
     print('F')

# score = int(input('수를 입력하세요'))

# if score >= 0:
#     print('짝수')

# elif score >= 0:
#      print('홀수')

# num = int(input('수를 입력하세요'))
# if num > 0:
#      print('num :',num)
#      if num % 2 == 0:
#           print('num은 짝수')
#      else:
#           print('num은 홀수')

# else:
#      print('num은 양수가 아니다')     


# user = input('입력값 :')
# result = 20+int(user)
# if result > 255 :
#     print(255)
# else:
#     print(result)


num = -5
if num > 0:
     print('num :',num)
     if num % 2 == 0:
          print('num은 양수')
     else:
          print('num은 음수')
else:
     print('num은 0이다') 

num = -5
if num > 0 :
     print('양수입니다.')
elif num < 0 :
     print('음수입니다.')
else :
     print('0입니다.')