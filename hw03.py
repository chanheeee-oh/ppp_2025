temp_c = int(input("온도를 입력하시오"))
temp_f = (temp_c * 9 / 5) + 32
print("{}C=>{}F".format(temp_c, temp_f))

import math

weight = int(input("몸무게를 입력하시오"))
height = int(input("키를 입력하시오"))
BMI = weight/pow(height/100, 2)
print(BMI)

import math
r = float(input("반지름을 입력하세요"))
pi = float(input("파이값을 입력하세요"))
area = pi*pow(r, 2)
print(area)

upper = int(input("윗변을 입력하세요"))
high = int(input("높이를 입력하세요"))
down = int(input("아랫변을 입력하세요"))
s = (upper+down)*high*0.5
s=(5+3)*4*0.5
print("s", s)

hanrabong = int(input("한라봉 그람수를 입력하세요"))
strawberry = int(input("딸기 그람수를 입력하세요"))
banana = int(input("바나나 그람수를 입력하세요"))
hanrabong_cal = (hanrabong / 100) * 50
strawberry_cal = (strawberry / 100) * 34
banana_cal = (banana / 100) * 77
hanrabong_kcal_per_100g = 50
strawberry_kcal_per_100g = 34
banana_kcal_per_100g = 77
total_cal = hanrabong_cal+strawberry_cal+banana_cal+hanrabong_cal
print(f"섭취한 총칼로리는 {total_cal}입니다.")

x1 = int(input("첫 번째 점의 x좌표를 입력하세요"))
y1 = int(input("두 번째 점의 y좌표를 입력하세요"))
x2 = int(input("세 번째 점의 x좌표를 입력하세요"))
y2 = int(input("네 번째 점의 y좌표를 입력하세요"))

distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
print(f" 두 점 사이의 거리는 {distance}입니다")



