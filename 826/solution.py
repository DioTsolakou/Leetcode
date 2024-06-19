from typing import List

def binary_search(max_profit_for_difficulty, target):
    left, right = 0, len(max_profit_for_difficulty) - 1
    while left <= right:
        mid = (left + right) // 2
        if max_profit_for_difficulty[mid][0] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return right

def max_profit_assignment(difficulty: List[int], profit: List[int], worker: List[int]) -> int:
    result = 0

    if len(difficulty) != len(profit):
        return 0
    
    diff_to_profit = sorted(zip(difficulty, profit))
    max_profit_for_difficulty = []
    max_profit = 0

    for d, p in diff_to_profit:
        max_profit = max(max_profit, p)
        max_profit_for_difficulty.append((d, max_profit))

    for i in range(len(worker)):
        diff_index = binary_search(max_profit_for_difficulty, worker[i])

        if diff_index >= 0 and worker[i] >= max_profit_for_difficulty[diff_index][0]:
            result += max_profit_for_difficulty[diff_index][1]

    return result



def main():
    diff, profit, workers = [2,4,6,8,10], [10,20,30,40,50], [4,5,6,7]
    result = max_profit_assignment(diff, profit, workers)
    print("\n"+str(result))


if __name__ == "__main__":
    main()