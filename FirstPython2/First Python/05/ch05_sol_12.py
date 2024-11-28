# 키보드로 부터 국어, 영어, 수학 점수를 입력받아 
# 평균 점수를 계산해 출력하는 코드를 코드 템플릿을 참고하여 작성하세요

koran = input('국어 점수를 입력하세요: ')
english = input('영어 점수를 입력하세요: ')
math = input('수학 점수를 입력하세요: ')

sub1 = int(input('국어 점수 : ','점'))
sub2 = int(input('영어 점수 : ','점'))
sub3 = int(input('수학 점수 : ','점'))
average = (sub1 + sub2 + sub3)/3 
print('평균점수 : ', round(average))




# korean = input('국어 점수를 입력하세요: ') #국어 점수를 입력하세요: 100
# english = input('영어 점수를 입력하세요: ') #영어 점수를 입력하세요: 90
# math = input('수학 점수를 입력하세요: ') #수학 점수를 입력하세요: 85

# print('국어 점수:', korean) #국어 점수: 100
# print('영어 점수:', english) #영어 점수: 90
# print('수학 점수:', math) #수학 점수: 85

# korean = int(korean)
# english = int(english)
# math = int(math)
# average = (korean + english + math) /3  
# print('평균 점수:', round(average)) #평균 점수: 92 #소수점 반올림