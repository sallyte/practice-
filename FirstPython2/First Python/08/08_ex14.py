# personInfo ={
#     '이름':'지훈',
#     '나이': 44,
#     '주소':'서울시 동대문구 11길 45로',
#     '취미':['낚시','요리','넷플릭스'],
#     '몸무게':77,
#     '혈액형': 'b',
#     '성별': '남'
# }

# print(personInfo['이름'])
# print(personInfo['취미'])
# print(personInfo['주소'])
# print(personInfo['성별'])


# dicContainer ={'이름':'홍길동',
#                '나이':25,
#                '주소':'서대문구 연희로2길 62',
#                '취미':['축구','수영','조깅'],
#                '몸무게':85.3

               
#                }
# print(dicContainer['주소','이름'])

# #튜플
# fruits =('apple','banana','plum','watrmelon','peach')
# fruits[1:4]
# print(type(fruits[1:4]))


# #딕셔너리
# # 20점 이상
# student = {'math':30,'science':18,'english':22, 'history':15}
# for key,value in student.items():
#     if value>20 :
#         print(key,value)



student = {'math':30,'science':18,'english':22, 'history':15}
sum = 0
for score in student.values():
    sum += score
    print('모든 점수합: ',sum)

# 딕셔너리 data에 있는 키를 알파벳 순으로 정렬
data = {"b": 2, "a": 1, "d": 4, "c": 3}
list = sorted(data.keys())
print(list)



