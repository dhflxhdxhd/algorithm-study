#1. 자료형
#number > 정수형, 실수형

#정수형 integer
a = 1000 #양의 정수
print(a)

a = -7 #음의 정수
print(a)

a = 0
print(a)

#실수형 Real Number
a = 8.14 #양의 실수
print(a)

a = -8.14 #음의 실수
print(a)

a = 8. #소수부가 0일때 0 생략
print(a)

a = -.7 #정수부가 0일때 0생략
print(a)

#지수표현 방식
a = 1e9 #or 1E9
print(a)

a = 81.15e1
print(a) #811.5

a = 814e-3
print(a) #0.814

#실수형 데이터 비교
#실수를 처리할 때 정확도가 떨어진다.
#데이터를 처리할 때 2진수를 이용하며 실수를 처리할 때 부동 소수점 방식을 사용하기 때문.
#예시
a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

#소수점 값을 비교하는 작업이 필요할 때  > round() 함수 이용.
#round(실수형 데이터, 반올림하고자 하는 위치 -1)
round(123.456,2) #123.46

#round() 함수 이용하여 실수형 데이터 비교
a = 0.3+0.6
print(round(a,2))

if round(a,2) == 0.9:
    print(True)
else:
    print(False)

#수 자료형 연산
#계산은 기본적으로 실수형 처리.
a = 7
b = 3

#나누기
print(a/b)

#나머지
print(a%b)

#몫
print(a//b)


