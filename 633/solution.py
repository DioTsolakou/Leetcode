import sys

def sum_of_square_nums(c: int) -> bool:
        a = 0
        while (a * a <= c):
            b = c - a * a
            if (binary_search(0, b, b)):
                return True
            a += 1
        
        return False
    
def binary_search(start, end, num) -> bool:
        if (start > end):
            return False
        
        mid = int(start + (end - start) / 2)

        if (mid * mid == num):
            return True
        
        if (mid * mid > num):
            return binary_search(start, mid - 1, num)
        
        return binary_search(mid + 1, end, num)

def main():
    #int_input = int(input)
    result = sum_of_square_nums(2)

    print(result)

if __name__ == '__main__':
    #main(sys.argv[1])
    main()