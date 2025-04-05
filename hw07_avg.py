import math

def average(nums):
   return sum(nums)/len(nums)

def main():
    numbers = [30, 77, 69, 100]
    avg = average(numbers)
    total = math.fsum(numbers)
    print(total)
    print(f"해당 숫자들의 평균은 {avg}입니다")

if __name__ == "__main__":
     main()


