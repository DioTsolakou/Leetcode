def reverse(x: int) -> int:
    str_x = str(x)
    is_negative = False

    if '-' in str_x:
        str_x = str_x.replace('-', '')
        is_negative = True

    reversed = str_x[::-1]

    if is_negative:
        reversed = '-' + reversed

    reversed = int(reversed)

    if reversed < pow(-2, 31) or reversed > pow(2, 31) - 1:
        return 0
    else:
        return reversed

    
def main():
    x = 123
    result = reverse(x)
    print("\n" + str(x))

if __name__ == "__main__":
    main()