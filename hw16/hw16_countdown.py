import time

def countdown(count):
    for remaining in range(count, 0, -1):
        print(f"{remaining}초 남았습니다...")
        time.sleep(1)
    print("무야호!")

def main():
    countdown(5)

if __name__ == "__main__":
    main()
