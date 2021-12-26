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

print("백문의 불여일견 \n백견이 불여일타")

# \", \' : 문장 내에서 따옴표(그냥 적을 경우 오류)
# 저는 "나도코딩"입니다.
print("저는 '나도코딩'입니다")
print('저는 "나도코딩"입니다')
print("저는 \"나도코딩\"입니다")

print("저는 \'나도코딩\'입니다")# \\ : 문장 내에서 \
print("c:\\Users\\USER\\Desktop\python\\practice.py")

# \r : 커서를 맨 앞으로 이동해서 "Red "을 "Pine"으로 대체 
print("Red Apple\rPine") 

# \b : 백스페이스 (한 글자 뒤로 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

# 퀴즈3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분을 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분을 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                     (nav)            (5)        (1)             (!)
# 예) 생성된 비밀번호 : nav51!

url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙 1
my_str = my_str[:my_str.index(".")] # my_str[0:5] -> 0 ~ 4 (0, 1, 2, 3, 4)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다".format(url, password))

# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway








