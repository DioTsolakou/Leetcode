from typing import List

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def search_insert(nums: List[int], target: int) -> int:
    if target > nums[-1]:
        return len(nums)
    if target < nums[0]:
        return 0
    
    return binary_search(nums, target)

def main():
    nums, target = [1,3,5,6], 7
    result = search_insert(nums, target)
    print("\n" + str(result))

if __name__ == "__main__":
    main()