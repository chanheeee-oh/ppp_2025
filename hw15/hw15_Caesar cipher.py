def caesar_encode(text: str, shift: int = 3) -> str:
    result = ""
    for ch in text:
        if 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += ch
    return result


def caesar_decode(text: str, shift: int = 3) -> str:
    return caesar_encode(text, -shift)

def main():
        print(caesar_encode("RIKu"))
        print(caesar_decode("kURi"))

if __name__ == "__main__":
    main()
