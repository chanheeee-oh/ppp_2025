import random
def problem():
    dan = random.randint(2,9)
    mul = random.randint(1, 9)
    try:
        ans = int(input(f"{dan} x {mul} = "))
    except ValueError:
        return False

    if ans == dan * mul:
        return True
    return False

def main():
    score = 0
    total_problem = 7
    for n in range(total_problem):
        is_correct = problem()
        if is_correct:
            score += 1
    print(f"총점은 {score}개 정답, {score / total_problem * 100:.0f}점")


if __name__ == "__main__":
    main()
