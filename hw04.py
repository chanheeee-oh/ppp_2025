weight = int(input("몸무게를 입력하시오"))
height = int(input("키를 입력하시오"))
BMI = weight/pow(height/100, 2)
if 23 <= BMI <= 24.9:
    print("비만 전단계입니다 건강하시네요")
elif 25 <= BMI <= 29.9:
    print("비만 1단계입니다 경고 1번!")
elif 30 <= BMI <= 34.9:
    print("비만 2단계입니다 경고 2번!!")
elif BMI >= 35:
    print("비만 3단계입니다 경고는 없습니다")

x1 = int(input("x좌표를 입력하세요"))
y1 = int(input("y좌표를 입력하세요"))

if x1 >= 0 and y1 >= 0:
    print("제1사분면입니다")
elif x1 <= 0 and y1 >= 0:
    print("제2사분면입니다")
elif x1 <= 0 and y1 <= 0:
    print("제3사분면입니다")
elif x1 >= 0 and y1 <= 0:
    print("제4사분면입니다")

hanrabong = int(input("한라봉 그람수를 입력하세요"))
strawberry = int(input("딸기 그람수를 입력하세요"))
banana = int(input("바나나 그람수를 입력하세요"))

kcal_per_100g = {"hanrabong" : 50, "strawberry" : 34, "banana" : 77}
hanrabong_cal = (hanrabong / 100) * 50
strawberry_cal = (strawberry / 100) * 34
banana_cal = (banana / 100) * 77

total_cal = hanrabong_cal+strawberry_cal+banana_cal+hanrabong_cal
print(f"섭취한 총칼로리는 {total_cal}입니다.")

import math
r = float(input("반지름을 입력하세요"))
pi = float(input("파이값을 입력하세요"))
area = pi*pow(r, 2)
circumference = 2 * pi * r
print(f"원의 면적은 {area:.2f} 이고 원의 둘레는 {circumference:.1f} 입니다")


