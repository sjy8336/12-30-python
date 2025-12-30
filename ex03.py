# 자료형 변환
# 변수가 참조하는 객체의 자료형을 다른 자료형으로 변환할 수 있다
# 변수 = 자료형 (값 or 변수)
# 실수 => 정수
x=int(3.14145) # 정수형으로 형변환(Casting)
print(x, type(x)) # 결과 => 3

# 정수 => 실수
y= float(10)
print(y, type(y))
print(x + y) # int + float => float     결과 => 13.0
#논리형(True/False) => 정수
b=True
c=False
print('True를 정수로: ', int(b))
# Ctrl + X : 현재 커서에 있는 한줄 삭제
print('False를 정수로: ', int(c))

# 문자열 => 정수/ 정수 => 문자열
var="abc"
var2="123"
# print(int(var))
# ValueError: invalid literal for int() with base 10: 'abc'
print(int(var2)*2)
m='하늘'
n='바다'
print(m, n)
tmp=' '
tmp= m # tmp = 하늘, m = 하늘
m = n
n = tmp
print(m, n) # 바다, 하늘
m, n = n, m
print(m, n) # 하늘, 바다
