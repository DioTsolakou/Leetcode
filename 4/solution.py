from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    merged_sorted_array = sorted(nums1 + nums2)
    length = len(merged_sorted_array)

    mid = length // 2

    if length > 2 and length % 2 != 0:
        return float(merged_sorted_array[mid])
    else:
        return float((merged_sorted_array[mid - 1] + merged_sorted_array[mid]) / 2)

def main():
    nums1, nums2 = [], [1,2,3,4,5]
    result = find_median_sorted_arrays(nums1, nums2)
    print("\n" + str(result))
    
if __name__ == "__main__":
    main()