print(2**3) #2^3 = 8 
print(5%3) # 나머지 구하기
print(10%3) # 1
print(5//3) # 몫 구하기

print(10 > 3)
print(4 >= 7)
print(10 < 3)
print(5 <= 5)

print(3 == 3)

print(1 != 3)
print (not (1 != 3))

print((3>0) and (3<5))
print((3>0) & (3<5))

print((3>0 or (3>5)))
print((3>0) | (3>5))

print(5>4>7)
print(5>4>2)

from cmath import sqrt
from math import ceil, floor


print(2+3*4)
print((2+3)*4)
number = 2+3*4
print(number)
number = number + 2 
print(number)
number += 2
print(number)
number *= 2 
print(number)
number /=2
print(number)
number -= 2 
print(number)
number %= 5
print(number)

print(abs(-5))
print(pow(4, 2 ))
print(max(5, 12))
print(min(5, 12))
print(round(3.14))
print(round(4.99))
from math import *
print(floor(3.14))
print(ceil(3.14))
print(sqrt(16))

from random import *
print(random()) # 0.0 ~1.0 미만의 임의의 값 생성
print(random()*10) 
print(int(random()*10))
print(int(random()*10)+1)
print(int(random()*45+1)) # 1~45 이하의 임의의 값 출력 
print(randrange(1, 46)) # 1~46 미만의 임의의 값 출력
print(randint(1,45)) # 1~45 이하의 임의의 값 출력

# 퀴즈

from random import *
number = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(number) + "일로 선정되었습니다.") # 숫자 or 참/거짓은 변수에 str()해야 출력 가능
