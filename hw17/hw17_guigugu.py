import random
import tkinter as tk
from tkinter import simpledialog, messagebox


def problem():
    dan = random.randint(2, 9)
    mul = random.randint(1, 9)

    try:
        ans = simpledialog.askinteger("구구단 문제", f"{dan} x {mul} = ?")
        if ans is None: 
            return None
        return ans == dan * mul
    except Exception:
        return False


def main():
    root = tk.Tk()
    root.withdraw()

    score = 0
    total_problem = 7

    for _ in range(total_problem):
        result = problem()
        if result is None:
            messagebox.showinfo("게임 종료", "게임이 취소되었습니다.")
            return
        elif result:
            score += 1

    messagebox.showinfo("결과", f"총점은 {score}개 정답, {score / total_problem * 100:.0f}점")


if __name__ == "__main__":
    main()
