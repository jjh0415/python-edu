sentence = '나는 손흥민 입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3= """
나는 소년이고,
파이썬은 쉬워요"""
print(sentence3)

jihwan = "960415-1234567"
print("성별 : " + jihwan[7]) # 컴터는 0부터 시작
print("연 : " + jihwan[0:2]) # 0~2 직전 까지
print("월 : " + jihwan[2:4])
print("일 : " + jihwan[4:6])
print("생년월일 : " + jihwan[:6]) #처음부터 6 직전까지
print("뒤 7자리 : " + jihwan[7:]) # 7부터 끝까지
print("뒤 7자리(역순) : " + jihwan[-7:])

python = "Python is Amazing"
print(python.lower())
print(python. upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))
print(python.find("java")) #원하는 값 없을시 -1
print(python.count("n"))

print("a" + "b")
print("a", "b")

print(" 나는 %d살 입니다." % 20) # d는 정수
print(" 나는 %s을 좋아해요." %"파이썬") # s는 문자열 , 숫자도 가능
print("Apple 은 %c로 시작해요."%"A") # c는 캐릭터, 한 글자만 받음

print("나는 %s색과 %s색을 좋아해요."%("파란", "빨간"))

print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20 , color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")

print("백문이 불여일견 \n백견이 불여일타") # \n : 줄바꿈
# 저는 "정지환" 입니다. 
print("저는 '정지환' 입니다")
print('저는 "정지환"입니다 ')
print("저는 \"정지환\" 입니다.") # \" \' : 문장에서 따옴표 역할

#\\ : 문장내에서 하나의 \
print("jeongjihwan$ \\usr\\local\\bin\\python3 ")

# \r : 커서를 맨앞으로 이동
print("Red Apple \rPine")

#\b : 백스페이스
print("Redd\bapple")

#\t : 탭
print("red\tapple")