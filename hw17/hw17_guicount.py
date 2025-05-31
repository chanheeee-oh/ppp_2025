import tkinter as tk

def countdown(label, count):
    if count > 0:
        label.config(text=f"{count}초 남았습니다...")
        count -= 1
        label.after(1000, countdown, label, count)
    else:
        label.config(text="무야호!")

def main():
    root = tk.Tk()
    root.title("카운트다운")

    label = tk.Label(root, font=("Arial", 30), text="")
    label.pack(padx=20, pady=40)

    countdown(label, 5)

    root.mainloop()

if __name__ == "__main__":
    main()
