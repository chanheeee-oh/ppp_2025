def txt3list(lines):
    nums = []
    for line in lines:
        for x in line.strip().split():
            nums.append(int(x))
    return nums

def average(nums):
    return sum(nums) / len(nums)

def max_riku(nums):
    return max(nums)

def min_riku(nums):
    return min(nums)

def median(nums):
    sorted_list = sorted(nums)
    n = len(sorted_list)
    if n % 2 == 1:
        return sorted_list[n // 2]
    else:
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2

def main():
    print("입력할 줄 수를 먼저 입력하세용용:")
    n = int(input())

    lines = []

    for i in range(n):
        line = input("숫자를 입력하세요: ")
        lines.append(line)

    nums = txt3list(lines)

    print("총 숫자의 개수는 {}".format(len(nums)))
    print("평균값은 {:.1f}".format(average(nums)))
    print("중앙값은 {}".format(median(nums)))
    print("최댓값은 {}".format(max_riku(nums)))
    print("최솟값은 {}".format(min_riku(nums)))

if __name__ == "__main__":
    main()
