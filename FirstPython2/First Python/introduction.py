# myName = '이설희'
# myMajor = '호텔경영'
# print('이설희 ,+myName,sep="|"')

# print("이름: 이설희")
# print("사는곳: 동대입구 근처")
# print("전공: 호텔경영")
# print("수강목적: 관련 취업 원하여")
# print("주변맛집: 글쎄요~찾아봐야 겠죠?")

file1 = open("introduction.txt","w")
names_list = []

while True:
    exit_input =input('계속하시겠습니까?(계속하려면 엔터, 종료하려면 "0"입력)')
    if(exit_input == '0') :
        print('프로그램을 종료합니다.')
        break

    myName = input('이름을 입력해 주세요')
    myHome = input('사는곳을 입력해 주세요')
    myMajor = input('전공을 입력해 주세요')

    names_list.append(myName)
    print('이름: ', myName, file = file1)
    print('사는곳: ', myHome, file = file1)
    print('전공: ', myMajor, file = file1)

print('입력된 이름 목록 :')
print(names_list)

file1.close()