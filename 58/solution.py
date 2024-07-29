def length_of_last_word(s: str) -> int:
    stripped_s = s.strip()
    words = stripped_s.split()

    return len(words[-1])


def main():
    s = 'luffy is still joyboy'
    result = length_of_last_word(s)
    print("\n " + str(result))

if __name__ == "__main__":
    main()