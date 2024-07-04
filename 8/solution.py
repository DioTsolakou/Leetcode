def my_atoi(s: str) -> int:
    new_str, result, sign_index = '0', 0, -1
    s = s.strip()
    
    for i in range(len(s)):
        if s[i] == '-' and i == 0:
            sign_index = i
        elif s[i] == '+' and i == 0:
            continue
        elif s[i].isdigit():
            new_str += s[i]
        else:
            break

    result = int(new_str)

    if sign_index == 0:
        result = int('-' + str(result))

    if result > pow(2, 31) - 1:
        result = pow(2, 31) - 1

    if result < pow(-2, 31):
        result = pow(-2, 31)

    return result

def main():
    s = "+1"
    result = my_atoi(s)
    print("\n" + str(result))

if __name__ == "__main__":
    main()