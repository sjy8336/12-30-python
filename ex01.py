# 주석
# ctrl + /
""" 
Shift + Alt + A
여러 라인 주석 처리하고 싶을 경우 사용
"""
'''
이것도 마찬가지
주석 처리 문자열
'''
# help(print)
""" print(*args, sep=' ', end='\n', file=None, flush=False) """
print('hi', 'python') 
print('hello', 'java', 'html', 'css', sep='@') 
# hello@java@html@css (위 결과물)
print('python\npython\npython')
""" 
(결과)
python
python
python
"""
print('java', 'java', 'java')
print('Script', 'Script', 'Script', sep='\n')
print('hi'*3, end=' ') # end='\n'이 기본값
print('Python~~')

# 'w'는 write
with open('out.txt', 'w') as f:
    print("Hello World~~", file=f)
    # out.txt파일에 출력된다. file=f -> 파일을 지정해야 print가 실행됨.
# 내려쓰기: Shift + tab 키
print(5+8)
print(10-3)
print(20*3)
print(100/2)

# 2+3=5
# print() 함수 이용해서 수식을 출력해봅시다
print('2', '+','3','=', 2+3)
# format() 함수 이용해 출력해보자
print('{0}+{1}={2}'.format(8, 2, 8+2))
print('{0} + {1} = {2}'.format(8, 2, 8+2))

# 변수
a=9
b=4
# f-string 추천
print(a, '-', b, a-b) # 이거 대신 쓰기 좋은게 f-string
print(f'{a} - {b} = {a-b}')

lat='35.7N'
lng='120.07E'
# 위도: 35.7N 경도: 120.07E
# 위 문자열을 출력하세요
print(f'위도: {lat}  경도: {lng}')

price=35000
print(price,'원')
print(str(price) + '원') 
# 변수 + 문자열 ==> 문자열 결합이 일어남
# 35,000원
# 형식 지정자
print(f'{price:,}원')
# {} 플레이스 홀더 내에 콜론(":")을 찍고 출력 크기와 형식을 지정
# 결과 -> 35,000원

pi=3.141592 # 실수 %f
r=10 # 정수 %d
print('반지름: %d, PI: %f' %(r, pi))
# 결과 => 반지름: 10, PI: 3.141592
print('반지름: %d, PI: %f' %(pi, r))
# 결과 => 반지름: 3, PI: 10.000000
# %d : 정수
# %f : 실수
# %s : 문자열
print('PI: %.2f' %pi) # 결과 => 3.14
# %전체자리수.소수점이하자리수f
print('%05.3f' %pi) # 소수점 포함 5자리 수가 나옴   결과 => 3.142
print('%07.2f' %pi) # 결과 => 0003.14

x="반갑습니다~"
z=55
y=789.14
# x, y, z 값들을 아래 형식으로 출력하세요
# x: 반갑습니다~
print('x: %s' %x) # %s에는 문자열, 숫자 모두 사용 가능
print('z: %s' %z)
print('y: %.1f' %y)