# # 애완동물을 소개해 주세요~
# animal = "고양이"
# name = "해피"
# age = 4
# hobby = "낮잠"
# is_adult = age >= 3

'''우리집 고양이의 이름은 해피예요
해피는 4살이며, 낮잠을 아주 좋아해요
해피는 어른일까요 True'''

# print("우리집 " + animal + "의 이름은 " + name + "예요")
# hobby = "공놀이"
''' 나중에 나온 hobby = "공놀이"로 설정됨 '''
# #print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
''' + 대신에 ,으로 연결해도 된다. 여기서  (name, "는 ")는 '해피 는'으로 출력됨'''
# print(name + "는 어른일까요?" + str(is_adult))

# Quiz) 변수를 이용하여 다음 문장을 출력하시오 #퀴즈1

# 변수명 
#  : station

# 변수값
#  : "사당", "신도림", "인천공항" 순으로 입력

# 출력 문장
#  : XX 행 열차가 들어오고 있습니다.

# station = "인천공항"
# print(station + "행 열차가 들어오고 있습니다") 

# print(1+1)
# print(2**3) #2^3 = 8
# print(5%3) #나머지 구하기 2
# print(5//3) #몫 구하기 1
# print(10//3) #3

# print(10 > 3)  #True
# print(4 >= 7) #False

# print(3 == 3) # True '=='는 앞에 값과 뒤에 값이 같은지 참,거짓 판별
# print(3 == 2) # False
# print(3 + 4 == 7) # True

# print(1 != 3) # True '!='는 앞에 값과 뒤에 값이 다르면 true
# print(not(1 != 3)) # not은 반대로 만드는 속성이다

# print((3 > 0) and (3 < 5)) # true  'and'는 앞에 항과 뒤에 항 모두 true여야 true
# print((3 > 0) & (3 < 5 )) # '&'는 'and'

# print((3 > 0) or (3 > 5)) # true 'or'은 앞,뒤 항 중 하나만 true면 true

# print(5 > 4 > 3) # true
# print(5 > 4 > 7) # false

# print(2 * 3 + 1)

# number = 2 + 8 + 4 # 14
# print(number)
# number = number + 2 # 16 number 값을 number + 2로 치환한다
# print(number)

# number += 2 # 18 위에 과정 생략
# print(number)

# number *= 2  # 36
# print(number)

# number %= 2 # 0
# print(number)

# print(abs(-5)) # 5 절댓값
# print(pow(4, 2)) # 4^2 = 4*4 = 16
# print(max(5, 12)) # 12
# print(min(5, 12)) # 5
# print(round(3.14)) # 3 반올림하는 'round'
# print(round(4.99)) # 5

# from math import *
# print(floor(4.99)) # 4 'floor'는 내림
# print(ceil(3.14)) # 올림 4
# print(sqrt(16)) # 제곱근 4 

'''from random import *

print(random()) # 0.0 ~ 1.0의 임의의 값 생성
print(random() * 10) # 0.0 ~ `10 미만의 임의의 값 생성(정수)
print(int(random() * 10))
print(int(random() * 10 + 1) # 1 ~ 10 임의의 값 설정

print(radrage(1, 45)) # 1 ~ 45 미만의 값 생성(1 ~ 44)

print(randint(1, 45)) # 1 ~ 45이하의 임의의 값 설정
작동 안됨

Quiz) 당신은 최근에  코딩 스터디 모임을 새로 만들었습니다 #퀴즈2
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다. 
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오

조건1 : 랜덤으로 날짜를 뽑아야 함
조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함 (아무리 늦어도 28일 이내의 날짜로 선정)
조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 설정되었습니다")

작동 안됨'''

# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)

# jumin = "990331-1234567"

# print("성별 : " + jumin[7]) # 첫번째 숫자를 0으로 해서 7의 값
# print("연 : " + jumin[0:2]) # 0 부터 2 직전까지 0 ~ 1
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])

# print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
# print("뒤 7자리 : " + jumin[7:]) # 7 부터 끝까지
# print("뒤 7자리 (뒤어서부터) : " + jumin[-7:])
# # 맨 뒤에서 7번째부터 끝까지

# python = "Python is Amazing"
# print(python.lower()) # 소문자화
# print(python.upper()) # 대문자화
# print(python[0].isupper())
# print(len(python)) #ㅍ글자수
# print(python.replace("Python", "Java"))
# # "Python"을 "Java"로 대체

# index = python.index("n")
# print(index)
# # n이 몇번째 있는지(5번째)
# index = python.index("n", index + 1)
# print(index)
# # n이 5 + 1 = 6번째이후로 몇번째 있는지

# print(python.find("Java")) # "Java"라는 단어를 찾아줌 만약 없으면 -1 표시
# # print(python.index("Java")) index는 찾는 단어가 없으면 오류남
# print(python.count("n")) # n이 2개 있다

# print("나는 %d살입니다" % 20)
# print("나는 %s을 좋아해요" % "파이썬")
# print("Apple은 %c로 시작해요." % "A")

# # %S 정수,문자 다 가능
# print("나는 %s살입니다" % 20)

# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨강"))

# # 방법2

# print("나는 {}살입니다.".format(20)) # 나는 20살입니다.
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨강"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨강")) #나는 빨강색과 파란색을 좋아해요
# # .format("파란", "빨강") "파란"이 0번째 "빨강"이 1번째

# # 방법3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))


# # 방법 4 (v3.6 이상~)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# print("백문의 불여일견 \n백견이 불여일타")

# # \", \' : 문장 내에서 따옴표(그냥 적을 경우 오류)
# # 저는 "나도코딩"입니다.
# print("저는 '나도코딩'입니다")
# print('저는 "나도코딩"입니다')
# print("저는 \"나도코딩\"입니다")

# print("저는 \'나도코딩\'입니다")# \\ : 문장 내에서 \
# print("c:\\Users\\USER\\Desktop\python\\practice.py")

# # \r : 커서를 맨 앞으로 이동해서 "Red "을 "Pine"으로 대체 
# print("Red Apple\rPine") 

# # \b : 백스페이스 (한 글자 뒤로 삭제)
# print("Redd\bApple")

# # \t : 탭
# print("Red\tApple")

# 퀴즈3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분을 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분을 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                     (nav)            (5)        (1)             (!)
# 예) 생성된 비밀번호 : nav51!

# url = "http://naver.com"
# my_str = url.replace("http://", "") # 규칙 1
# my_str = my_str[:my_str.index(".")] # my_str[0:5] -> 0 ~ 4 (0, 1, 2, 3, 4)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀번호는 {1}입니다".format(url, password))

# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# # 조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# # 하하씨가 다음 정류장에서 다음 칸에 탐
# # append 뒤에 추가
# subway.append("하하")
# print(subway)

# # 정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1, "정형돈")
# print(subway)

# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# # 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# # 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# # 다양한 자료형 함께 사용
# mix_list = ["조세호", 20, True]

# # 리스트 확장
# num_list = [5,2,4,3,1]
# num_list.extend(mix_list)
# print(num_list)

# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# # [],.get()을 이용해 값을 출력할 수 있다
# # 그러나 값이 없을 때 []는 오류가 나고 .get()는 none이라고 출력됨
# # .get(5, "사용가능")이라고 쓰면 none 대신 사용가능이 출력
# print(cabinet.get(5))
# print(cabinet.get(5, "사용가능"))
# print("hi")

# print(3 in cabinet) # True, 3이라는 키가 "cabinet" 안에 있는가?
# print(5 in cabinet) # False

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# # 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# # 간 손님
# del cabinet["A-3"]
# print(cabinet)

# # key들만 출력
# print(cabinet.keys())

# # value들만 출력
# print(cabinet.values())

# # key, value 쌍으로 출력
# print(cabinet.items())

# # 모두 삭제
# cabinet.clear()
# print(cabinet)

''' 5-3 튜플'''
''' 5-3 튜플'''
''' 5-3 튜플'''

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# 튜플에서는 추가가 안된다
# menu.add("생선까스")

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

'''5-4 세트'''
'''5-4 세트'''
'''5-4 세트'''

# # 집합 (set)
# # 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합 (java 와 python을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))

# # 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))

# # 차집합 (java 할 수 있지만 python은 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))

# # python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java를 잊었어요
# java.remove("김태호")
# print(java)

'''5-5 자료구조의 변경'''
'''5-5 자료구조의 변경'''
'''5-5 자료구조의 변경'''

# 자료구조의 변경
# 커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

'''5-6 퀴즈 4'''
'''5-6 퀴즈 4'''
'''5-6 퀴즈 4'''

# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복은 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)
#  -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
#  -- 축하합니다 --

# from random import *
# st = [1,2,3,4,5]
# print(st)
# shuffle(st)
# print(st)
# print(sample(st,1))

# from random import *
# users = range(1, 21) # 1부터 20까지 숫자를 생성
# print(type(users))
# users = list(users)
# print(type(users))

# shuffle(users)
# print(users)

# winners = sample(users, 4) # 4명 중에서 1명을 치킨, 3명은 커피

# print(" --당첨자 발표-- ")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print(" -- 축하합니다 -- ")

'''6-1 if'''
'''6-1 if'''
'''6-1 if'''

# # 'input'은 터미널에서 입력하면 그 값에따라 출력된다
# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요, 나가지 마세요")
# elif 10 <= temp and temp <30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요, 나가지 마세요")

'''6-2 for'''
'''6-2 for'''
'''6-2 for'''

'''for waiting_no in range(5) # 0, 1, 2, 3, 4 range(1, 6) => 1, 2, 3, 4, 5
    print("대기번호 : {0}".format(waiting_no)) 
    
    작동안됨'''

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

'''6-3 while'''
'''6-3 while'''
'''6-3 while'''

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다")

# customer = "아이언맨" # while True를 쓰면 무한루프에 빠진다, 무한루프에 빠지면 작동중지하면 된다 (ctrl + c) 
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer :
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")

'''6-4 continue & break'''
'''6-4 continue & break'''
'''6-4 continue & break'''

# # 2,5을 패스하고 계속 이어나간다(continue)
# absent = [2, 5] # 결석
# for student in range(1, 11): # 1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue
#     print("{0}, 책을 읽어봐".format(student))

# # break => 중지
# absent = [2, 5] # 결석
# no_book = [7] # 책X
# for student in range(1, 11): # 1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지, {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

'''6-5 한 줄 for'''
'''6-5 한 줄 for'''
'''6-5 한 줄 for'''

# # 출석번호가 1, 2, 3, 4, 5 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# # 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# # 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

'''6-6 퀴즈5'''
'''6-6 퀴즈5'''
'''6-6 퀴즈5'''

# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [  ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분) 
# ...
# [  ] 50번째 손님 (소요시간 : 16분) 

# 총 탑승 승객 : 2 분

# from random import *
# cnt = 0 # 총 탑승 승객 수
# for i in range(1, 51):  # 1 ~ 50 이라는 수(승객)
#     time = randrange(5, 51) # 5분 ~ 50분 소요 시간
#     if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님 (매칭 성공), 탑승 승객 수 증가 처리
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else: # 매칭 실패한 경우
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

# print("총 탑승 승객 : {0} 분".format(cnt))

'''7-1 함수'''
'''7-1 함수'''
'''7-1 함수'''

# def는 함수를 설정한다, 함수를 적어야 작동한다
# def open_account():
#     print("새로운 계좌가 생성되었습니다")

# open_account()

# '''7-2 전달값과 반환값'''
# '''7-2 전달값과 반환값'''
# '''7-2 전달값과 반환값'''

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다".format(balance + money))
#     return balance + money

# def withdraw(balance, money): #출금
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission

# balance = 0 # 잔액 == 0
# balance = deposit(balance, 1000)
# print(balance)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
# balance = deposit(balance, 3000)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1} 원입니다".format(commission, balance))

'''7-3 기본값'''
'''7-3 기본값'''
'''7-3 기본값'''

# 같은 나이, 잘하는 것도 같다
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
        .format(name, age, main_lang))

profile("유재석")






















