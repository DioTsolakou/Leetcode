from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    num_dict = dict()
    result = [-1, -1]

    for i in range(len(nums)):
        if (target - nums[i] in num_dict):
            result[1], result[0] = i, num_dict[target - nums[i]]
            return result
        
        num_dict[nums[i]] = i

    return result

def main():
    nums, target = [2, 7, 11, 15], 9
    result = two_sum(nums, target)
    print(result)

if __name__ == "__main__":
    main()