def total_calorie(fruits, fruits_calorie_dic):
    total = 0
    for fruit in fruits:
        weight = fruits[fruit]
        calorie_per_100g = fruits_calorie_dic.get(fruit, 0)
        total += (weight / 100) * calorie_per_100g
    return total

def main():
    strawberry_eat = int(input("딸기를 섭취한 그람수를 입력하세요"))
    hanrabong_eat = int(input("한라봉을 섭취한 그람수를 입력하세요"))

    fruits = {"strawberry": strawberry_eat, "hanrabong": hanrabong_eat}
    fruits_calorie_dic = {"hanrabong":50, "strawberry": 34, "banana": 77}
    total = total_calorie(fruits, fruits_calorie_dic)
    print(f"섭취한 총칼로리는 {total:.2f} kcal 입니다")

if __name__ == "__main__":
    main()

