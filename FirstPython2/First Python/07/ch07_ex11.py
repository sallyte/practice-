# while not False:
#     print('hello~')

# print(not False)

# txt = 'welcome to the jungle'
# x =txt.find('welcome')
# print(x)

# numbers = [1, 2, 3, 4, 5]
# total = 0

# for a in numbers:
#     total += a
#     print(total)

# numbers = [10,20,30,40,50]
# numbers.sort()
# print(numbers)

# max_num = numbers[-1]
# print(max_num)

# numbers = [10,20,30,40,50]
# max_num = 0

# for a in numbers :
#     if a > max_num :
#         max_num = a
# print(max_num)

# print(numbers.index(30))

# # str ='python'
# # print(str.index('th'))

# numbers.append(100)
# print(numbers)

# numbers.insert(1,15)  #(1)인덱스에 15추가 기입
# print(numbers)

# list1 = [1,2,3]
# list2 = [10,20,30]

# list1.extend(list2)  #list1,2 연장하기
# print(list1)

# list1.pop(1)  #인덱스 (1)아이템 삭제하기
# print(list1)

# list1.remove(10)  # 특정아이템 삭제하기
# print(list1)

# infos = ['홍길동',20,'서울시종로구','독서','0형']  #문자열 길이(갯수) 구하기
# print(len(infos))   


# toDoList =['cleaning','shopping','TOEIC study','exercise']
# print('오늘 할 일 : ', toDoList)

# for i in range(len(toDoList)):
#     print('끝난 일 : ',toDoList.pop(0))
#     if len(toDoList) != 0 :
#         print('남은 일 :', toDoList)
#     else:
#         print('오늘 할일 끝')


# animals = ['호랑이','사자','곰','여우','늑대']
# animals[1:4]
# print(animals[1:4])  #슬라이싱 (1)이상(4)미만


# my_tuple1 =(1,2,3,4,5)
# my_tuple2=(10,20,30,40,50)

# print(my_tuple[3])
# print(len(my_tuple)-1)
# if(1 in my_tuple) :  #1이 들어 있나?
#     print('1')


# my_tuple1 =(1,2,3,4,5)
# sorted(my_tuple1)


# 1. 리스트 합 구하기
# 투플의 들어있는 숫자들의 합을 구하시오.
numbers = (1, 2, 3, 4, 5)
total = 0

for a in numbers:
    total += a
    print(total)