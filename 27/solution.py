def removeElement(nums: [int], val: int) -> int:
    length = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[length] = nums[i]
            length += 1
    
    return length, nums



def main():
    nums, val = [3,2,2,3], 3
    result1, result2 = removeElement(nums, val)
    print("\n Not equal:" + str(result1) + "\n nums=" + str(result2))

if __name__ == "__main__":
    main()