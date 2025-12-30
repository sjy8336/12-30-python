# 연산자
""" 
연산자 종류
[1] 산술 연산자 : +, -, *, /, //, %, **(거듭제곱)
[2] 관계 연산자 : ==, !=, >, >=, <, <=
[3] 논리 연산자 : and, or, not
[4] 대입 연산자 : =
[5] 할당 연산자 : +=, -=, *=, /= 등
[6] 멤버쉽 연산자 : in, not in
[7] 비트 연산자 : &, |, ^, ~, <<, >>
"""
a=8
b=5
print(a+b, a-b, a*b, a/b) # 결과 => 13 3 40 1.6
print(a//b) # 1 나눈 후 정수 부분만 취합
print(a%b)
print(a**2) # 8 의 제곱 => 64
# 연산자 우선순위
x, y, z = 2, 4, 5
print(x+y-z) # 1
print((x+y)*z) # 22 => 30
print(x**2+z//2) # 6

# 관계 연산자 
# == (값이 같으면 True, 다르면 False)
# != (값이 다르면 True, 같으면 False)
# > (크냐?), >= (크거나 같으나)
# < (작냐?), <= (작거나 같으나)
x=6
y=6.0
z=8
q=3
print(f'x={x}, y={y}, z={z}, q={q}')
print(f'x==y: {x==y}')
print(f'x!=y: {x!=y}')
print(f'x<=y: {x<y}')
print(f'x>=y: {x>y}')
print(f'z>q: {z>q}, z<q: {z<q}')

# 논리 연산자 : and, or, not 연산자
# 논리값을 가지고 연산함
print('--논리 연산자----')
# and 연산자: 피연산자 2개가 모두 True일 경우 True
print(True and True) 
print(True and False)
print(False and True)
print(False and False)

# or연산자: 피연산자 2개가 모두 False일 경우만 False
print('-----------------')
print(True or True) 
print(True or False)
print(False or True)
print(False or False) # False
print('---not -----')
isLogin=False
print(f'isLogin: {not isLogin}')
# not : True값은 False로 / False는 True로 논리 부정 연산
# 할당 연산자 (연산 후 대입 연산자)
# +=, -=, *=, /=, //=, %=
a=3 # 대입 연산자
print(a) #3
a=a+1
print(a) #4
a+=1 # a=a+1 과 동일함
print(a)
a+=3 # 3만큼씩 누적
print(a)
a-=1 # 1만큼씩 차감
print(a)
a*=3 # a= a*3
print(a)
a//=4
print(a)
a/=3
print("%.2f" %a)
a*=8
print(a)
a=int(a) #13
a**=2 # 13^2
print(a)
# 멤버쉽 연산자
""" 
in 문자열 / 리스트 / 튜플 :
문자열이나 리스트, 튜블에 지정한 값이 있으면 True
없으면 False를 반환함
not in:  
"""

# (): 소괄호, {}: 중괄호, []: 대괄호
arr=[10, 20, 30, 40, 50] # list
print(arr)
print(30 in arr) # True
print(90 in arr) # False

print(10 not in arr) # False
print(90 not in arr) # True
var="apple"
print(var)
print('app' in var) # True
print('app' not in var) # False