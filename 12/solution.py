def int_to_roman(num: int) -> str:
    result = ''

    if num > 3999 or num < 1:
        return 0

    int_to_roman_tuples = [
        (1000, 'M'),
        (500, 'D'),
        (100, 'C'),
        (50, 'L'),
        (10, 'X'),
        (5, 'V'),
        (1, 'I')
    ]

    str_num = str(num)

    l, r = 0, len(str_num)

    while l < r:
        curr_num = int(str_num[l] + '0' * (r - l - 1))
        curr_roman = ''

        for i in range(len(int_to_roman_tuples)):
            curr_tuple = int_to_roman_tuples[i]
            if curr_num >= curr_tuple[0]:
                times = (curr_num // curr_tuple[0])
                curr_roman += times * curr_tuple[1]

                if str_num[l].startswith(('4', '9')):
                    prev_tuple = int_to_roman_tuples[i - 1]
                    result += dict(int_to_roman_tuples)[prev_tuple[0] - curr_num] + prev_tuple[1]
                    break

                leftover = curr_num % curr_tuple[0]
                if leftover == 0:
                    result += curr_roman
                    break
                else:
                    curr_num = leftover



        l += 1

    return result

def main():
    num = 3749
    result = int_to_roman(num)
    print("\n" + result)

if __name__ == "__main__":
    main()