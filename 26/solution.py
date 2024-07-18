from typing import List


def removeDuplicates(nums: List[int]) -> int:
    num_set = set()

    for i in range(len(nums)):
        if nums[i] in num_set:
            nums[i] = 101
        else:
            num_set.add(nums[i])
    
    nums.sort()
    return len(num_set), nums

def main():
    nums = [1,1,2]
    result1, result2 = removeDuplicates(nums)
    print("\nUnique:" + str(result1) + "\n nums=" + str(result2))


if __name__ == "__main__":
    main()