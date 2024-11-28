# # p152
h = int(input('키를 입력하세요(cm)'))
w = int(input('몸무게를 입력하세요(km)'))

h = h/100
b = w/(h**2)

if b >= 0 and b < 18.5 :
    print('저체중',b)
elif b >= 18.5 and b < 23 :
    print('정상',b)
elif b >= 23 and b < 25 :
    print('비만전단계',b)
elif b >= 25 :
    print('비만',b)


# a1 = True
# a2 = True
# if a1 == :
#     print('True')

# height = int(input('키를 입력해 주세요: '))
# # print(height >= 120 and  height < 170)
# str = '탑승 가능' if height >=120 else '탑승 불가능'  #조건식
# print(str)

# if (height >= 120) and (height < 170) :
#     print('탑승 가능')
# else :
#     print('탑승 불가능')