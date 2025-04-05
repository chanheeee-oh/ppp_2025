def get_range_list(n):
    return list(range(1, n))

def main():
    n = int(input("숫자를 입력하세요"))
    result = get_range_list(n)
    print(f"1부터 {n-1}까지의 리스트에서 {result}까지의 값")
if __name__ == "__main__":
     main()
