import random
import tkinter as tk
from tkinter import simpledialog, messagebox

def check(solution, answer, input_ch):
    is_correct = False
    for i in range(len(solution)):
        if solution[i] == input_ch:
            answer[i] = solution[i]
            is_correct = True
    return is_correct

def main():
    root = tk.Tk()
    root.withdraw()

    problems = ["apple", "banana", "grape", "melon"]
    solution = random.choice(problems)
    answer = ["_" for _ in range(len(solution))]

    trial = 7
    is_correct = False

    while True:
        current_state = " ".join(answer)
        input_ch = simpledialog.askstring("문자 입력", f"{current_state} (남은 시도: {trial})\n\n한 글자를 입력하세요:")

        if input_ch is None:
            messagebox.showinfo("게임 종료", "게임이 취소되었습니다.")
            return

        input_ch = input_ch.lower().strip()

        if len(input_ch) != 1 or not input_ch.isalpha():
            messagebox.showwarning("입력 오류", "한 글자만 입력하세요!")
            continue

        if check(solution, answer, input_ch):
            messagebox.showinfo("결과", f"'{input_ch}'가 포함되어 있습니다!")
        else:
            trial -= 1
            messagebox.showinfo("결과", f"틀렸습니다! (남은 시도: {trial})")

        if "_" not in answer:
            is_correct = True
            break
        if trial == 0:
            break

    if is_correct:
        messagebox.showinfo("게임 결과", f"정답입니다! 단어: '{solution}'")
    else:
        messagebox.showinfo("게임 결과", f"게임오버! 정답은 '{solution}'였습니다.")

if __name__ == "__main__":
    main()
