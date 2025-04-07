def gugudan(num):
    for i in range(9):
     print(f"{num} x {i + 1} = {num * (i + 1)}")

if __name__ == "__main__":
    num = int(input("구구단을 낉여와라:"))
    gugudan(num)


