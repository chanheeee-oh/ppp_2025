import random
CHO = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
def extract_chosung(word):
    result = []
    for ch in word:
        if '가' <= ch <= '힣':
            base = ord(ch) - ord('가')
            chosung_index = base // (21 * 28)
            result.append(CHO[chosung_index])
        else:
            result.append(ch)
    return ''.join(result)

def main():
    words = ["시온", "유우시", "리쿠", "재희", "료", "사쿠야"]
    selected_word = random.choice(words)
    chosung_hint = extract_chosung(selected_word)

    print("힌트: 엔시티 위시(NCT WISH) 멤버 이름이에요!")
    print(f" 초성 힌트: {chosung_hint}")
    user_guess = input("단어를 맞춰보세요: ")

    if user_guess == selected_word:
        print("💚 정답입니다!")
    else:
        print(f"❌ 틀렸습니다. 정답은 '{selected_word}'입니다.")


if __name__ == "__main__":
    main()