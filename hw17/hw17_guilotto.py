import random
import tkinter as tk
from tkinter import simpledialog, messagebox

def get_lotto():
    lotto = []
    while len(lotto) < 6:
        n = random.randint(1, 45)
        if n not in lotto:
            lotto.append(n)
    return sorted(lotto)

def main():
    root = tk.Tk()
    root.withdraw()

    try:
        count = simpledialog.askinteger("입력", "몇 세트의 로또 번호를 생성할까요?")
        if count is None or count <= 0:
            raise ValueError

        result = ""
        for i in range(count):
            result += f"Set {i + 1}: {get_lotto()}\n"

        messagebox.showinfo("로또 번호", result)

    except ValueError:
        messagebox.showerror("오류", "양의 정수를 입력해 주세요.")

if __name__ == "__main__":
    main()
