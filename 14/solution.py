from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    result, char_dict = '', dict()

    for i in strs:
        for j in i:
            char_dict.update({ j: char_dict[j] + 1 if j in char_dict else 1 })

    for k, v in char_dict.items():
        if v == len(strs):
            result += k
        else:
            break

    return result

def main():
    strs = ["aa","aa"]
    result = longestCommonPrefix(strs)
    print("\n" + result)

if __name__ == "__main__":
    main()
