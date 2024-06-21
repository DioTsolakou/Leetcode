def is_palindrome(x: int) -> bool:
    str_num = str(x)
    str_len = len(str_num)
    reverse_str = ['0']*str_len

    for i in range(str_len):
        reverse_str[str_len - i - 1] = str_num[i]

    return ''.join(reverse_str) == str_num

def is_palindrome_pythonic(x: int) -> bool:
    reversed = str(x)[::-1]
    return reversed == str(x)

def main():
    x = -121
    result = is_palindrome(x)
    result_2 = is_palindrome_pythonic(x)
    print("\n" +str(result))
    print("\n" +str(result_2))

if __name__ == "__main__":
    main()