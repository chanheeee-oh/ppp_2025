def kcal(hanrabong, strawberry, banana):
    hanrabong_cal = (hanrabong / 100) * 50
    strawberry_cal = (strawberry / 100) * 34
    banana_cal = (banana / 100) * 77
    total_cal = hanrabong_cal + strawberry_cal + banana_cal
    return total_cal

def main():
    hanrabong = int(input("한라봉 그람수를 입력하세요: "))
    strawberry = int(input("딸기 그람수를 입력하세요: "))
    banana = int(input("바나나 그람수를 입력하세요: "))

    total_calories = kcal(hanrabong, strawberry, banana)
    print(f"섭취한 총 칼로리는 {total_calories:.2f} kcal 입니다.")

if __name__ == "__main__":
    main()



