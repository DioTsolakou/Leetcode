def strStr(haystack: str, needle: str) -> int:
    if len(needle) > len(haystack):
        return -1

    l, r = 0, len(needle)
    while l < r and l < len(haystack) - len(needle) + 1:
        if haystack[l:r] == needle:
            return l
        else:
            l += 1
            r += 1
    
    return -1


def main():
    haystack, needle = "mississippi", "issi"
    result = strStr(haystack, needle)
    print("\n" + str(result))

if __name__ == "__main__":
    main()