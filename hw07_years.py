def is_leap_year(y):
    if y % 4 == 0:
        if y % 100 == 0: #100으로 나누어 떨어지면 윤년이 아님
           return False
        return True #4로 나누어떨어짐
    return False #4로 안 나눠질 때


def main():
    year = int(input("숫자를 입력하세요"))
    if is_leap_year(year):
        print(f"{year}는 윤년입니다")
    else:
        is_leap_year(year)
        print(f"{year}년도는 윤년이 아닙니다")

if __name__ == "__main__":
     main()
