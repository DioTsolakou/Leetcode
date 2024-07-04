def length_of_longest_substring(s: str) -> int:
    substr_set = set()
    substr_len, j = 0, 0

    for i in range(len(s)):
        if s[i] not in substr_set:
            substr_set.add(s[i])
            substr_len = max(substr_len, i - j + 1)
        else:
            while s[i] in substr_set:
                substr_set.remove(s[j])
                j +=1
            substr_set.add(s[i])


    return substr_len

def main():
    string = "abcabcbb"
    result = length_of_longest_substring(string)
    print("\n" + str(result))

if __name__ == "__main__":
    main()