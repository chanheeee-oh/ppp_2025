import math

def average(nums):
   return sum(nums) / len(nums)

def main():
    chanhui_input = input("숫자를 입력하세요")

    split_numbers = chanhui_input.split()
    print(split_numbers)

    numbers = []
    for num in split_numbers:
        numbers.append(float(num))
    print(numbers)

    avg = average(numbers)
    total = math.fsum(numbers)
    print(total)
    print(f"해당 숫자들의 평균은 {avg}입니다")


if __name__ == "__main__":
     main()

