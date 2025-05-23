import random

def check(solution, answer, input_ch):
    is_correct = False
    for i in range(len(solution)):
        if solution[i] == input_ch:
            answer[i] = solution[i]
            is_correct = True
    return is_correct

def main():
    problems = ["apple", "banana", "grape", "melon"]
    solution = random.choice(problems)
    answer = ["_" for _ in range(len(solution))]

    trial = 7
    is_correct = False

    while True:
        print(" ".join(answer), f"(trial={trial})")
        input_ch = input("답을 입력하시오 => ").lower().strip()

        if len(input_ch) != 1 or not input_ch.isalpha():
            print("한 글자만 입력하세요!\n")
            continue

        if check(solution, answer, input_ch):
            print(f"{input_ch}가 포함되어 있습니다.\n")
        else:
            trial -= 1
            print(f"틀렸습니다.\n")

        if "_" not in answer:
            is_correct = True
            break

        if trial == 0:
            break

    if is_correct:
        print("정답입니다!")
    else:
        print(f"게임오버! 정답은 '{solution}'였습니다.")

if __name__ == "__main__":
    main()
