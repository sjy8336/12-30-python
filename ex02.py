""" 
변수란?
- 데이터를 일시적으로 보관하거나 처리 결과를 담을 수 있는 기억 장소
    => 실제 값을 저장하는 메모리 이름
- variable, field, property 라고 한다
- 변수에 저장하는 값들을 literal이라고 한다
"""
a=10
#  = : 대입 연산자/할당 연산자
# == : 비교 연산자. 값을 비교함
# a---------->{메모리주소값:10}
# a변수에는 메모리 주소값이 할당되고 해당 주소에 10이라는 값이 저장되어 있는 형태
print(f"a의 값은 {a}입니다")
print(f"a의 주소값은 {id(a)}입니다")
"""파이썬 자료형(data type)
[1] 숫자 타입 (Numeric): 정수 int (크기: 무제한)/실수 float (8byte)
[2] 문자열 타입 (Character): 문자, 문자열 str (크기: 무제한)
[3] 불린 타입 (Logical): 참(True), 거짓(False) bool
"""
b1=123
c=57.89
var1="Python"
d=True
# 1b=456 [x] 숫자로 시작해선 안된다. 특수문자 사용불가.
# @@@=789 [x]
# 각 변수의 값과 타입을 출력하세요
print(b1, type(b1))
print(c, type(c))
print(var1, type(var1))
print(d, type(d))
x=100
print(x, type(x)) # int
x='bye~'
print(x, type(x)) # str
# 동적 변수 : 변수에 대입하는 값에 따라 자료형이 변화한다
a=123
b=345
print(a, b)
a, b = b, a
print(a, b)
x, y, z = 1, 2, 3
print(x, y, z)
# 변수 명명법
""" 
- 첫문자는 영문자로 시작. 숫자로 시작 X
- 공백이나 특수문자 사용 안함. 언더바(_)는 사용 가능
- 예약어(keyword) 사용하면 안된다
- 대소문자 구분
- 두 단어 이상 변수로 사용할 때는 camel표기법 HlloWorld
                            snake표기법 hello world
"""
s1="오늘도 "
s2="즐거운 하루!!"
s3=365
print(s1+s2) # : 문자열 결합 연산자
print(s1+str(s3)) # TypeError +: 문자열끼리만 결합 가능
# str(s3) : int형을 str형으로 형변환함
m=100
w,e,r=1,2,3
a=b=c=d=100
print(a,b,c,d)

strVar='1번라인\n2번라인\n3번라인'
print(strVar)
strVar2="""
1. 첫째줄
2. 둘째줄
3. 셋째줄
"""
print(strVar2)

# 자신의 이름, 몸무게, 나이를 변수로 선언하고 값을 대입한 후 결과를 출력하세요
# 아래 포맷으로 출력하세요
""" 
이름: 김철수
나이: 22세
몸무게: 66kg
"""
k="""
이름: 김철수
나이: 22세
몸무게: 66kg
"""
print(k)

name="김철수"
age="22"
kg="66"
print(f'이름: {name}\n나이: {age}세\n몸무게: {kg}kg')
print(f"""
이름: {name}
나이: {age}세
몸무게: {kg}kg
""")

# print() 함수: 출력하는 함수
# input() 함수: 입력받는 함수
Age = input('당신의 나이를 입력하세요=>')
print(f'당신은 {Age}세 이군요', type(Age))
# 당신은 22세 이군요 <class 'str'>
# 10년 뒤 당신은 33세이군요
# print(f'10년 뒤 당신은 {Age+str(10)}세 이군요!!') int 타입을 str로 바꿔준거임
print(f'10년 뒤 당신은 {int(Age)+10}세 이군요!!')
# str을 int형으로 형변환하여 연산하자!
# 형변환: 정수형-=> int() / 실수형 float() / 문자열 str()
""" 
[1] 이메일과 아이디, 비밀번호를 입력 받고 아래와 같이 출력하세요
Hong 고객님 안녕하세요?
Hong 님의 이메일과 비밀번호는 아래와 같습니다
email: hong@naver.com
password: 123

[2] 국어, 영어, 수학 점수를 입력받고
합계 점수와 평균 점수를 출력하세요
"""

ID = input('아이디를 입력하세요 =>')
email = input('이메일을 입력하세요 =>')
PW = input('비밀번호를 입력하세요 =>')
print(f"""
{ID} 고객님 안녕하세요?
{ID} 님의 이메일과 비밀번호는 아래와 같습니다
email: {email}
password: {PW}
""")

# 내가 한거
# Kor = input('국어 점수를 입력하세요 =>')
# Eng = input('영어 점수를 입력하세요 =>')
# Math = input('수학 점수를 입력하세요 =>')
'''print(f"""
합계 점수는 {int(Kor)+int(Eng)+int(Math)}이고, 
평균 점수는 {int(Kor)+int(Eng)+int(Math)/3}
""")'''

kor = input('국어 점수 입력 =>')
eng = input('영어 점수 입력 =>')
math = input('수학 점수 입력 =>')
total = float(kor) + float(eng) + float(math)
avg = total/3
print(f'''
국어: {kor}
영어: {eng}
수학: {math}
--------------
합계 점수: {total}점
평균 점수: {avg}점
''')