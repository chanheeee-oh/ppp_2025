def exc():
    numbers = []

    while True:
        kuri_input = input("무엇이든 입력해보세용")
        if kuri_input == '-1':
            break
        try:
            num = int(kuri_input)
            if num > 0:
               numbers.append(num)
        except ValueError:
            continue
    return numbers


def main():
    numbers = exc()
    count = len(numbers)
    average = sum(numbers) / count if count > 0 else 0

    print(f"입력된 값은 {numbers}입니당")
    print(f"자연수는 {count}개가 있고요")
    print(f"평균은 {average}입니듀듀듀듀")



if __name__ == "__main__":
    main()



