from typing import List


def plus_one(digits: List[int]) -> List[int]:
    joined_digits = int("".join(map(str, digits)))
    joined_digits += 1    

    return list(map(int, str(joined_digits)))

def main():
    digits = [9]
    result = plus_one(digits)
    print("\n " + str(result))

if __name__ == "__main__":
    main()