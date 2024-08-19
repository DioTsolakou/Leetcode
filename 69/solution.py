class Solution:
    def my_sqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        start, end = 1, x
        while start <= end:
            mid = start + (end - start) // 2

            mid_sq = mid * mid

            if mid_sq == x:
                return mid
            elif mid_sq > x:
                end = mid - 1
            else:
                start = mid + 1

        return end

def main():
    x = 8
    result = Solution.my_sqrt(Solution, x)
    print("\n" +str(result))

if __name__ == "__main__":
    main()