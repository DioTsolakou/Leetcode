from typing import List


""" def max_satisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
    l, r, max_cust = 0, minutes, 0

    curr_max_cust = 0
    max_window = '0' + str(minutes)
    while l <= r and r <= len(customers):
        curr_cust_sum = sum(customers[l:r])

        if curr_cust_sum > curr_max_cust and 1 in grumpy[l:r]:
            curr_max_cust = curr_cust_sum
            max_window = str(l) + str(r)
        
        l += 1
        r += 1
    
    for i in range(int(max_window[0]), int(max_window[1])):
        grumpy[i] = 0

    for j in range(len(customers)):
        if grumpy[j] == 0:
            max_cust += customers[j]

    return max_cust """

def max_satisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
    curr_unsat_cust, sat_cust = 0, 0

    for i in range(minutes):
        curr_unsat_cust += customers[i] * grumpy[i]

    max_unsat_cust = curr_unsat_cust

    for i in range(minutes, len(customers)):
        curr_unsat_cust += customers[i] * grumpy[i]
        curr_unsat_cust -= customers[i - minutes] * grumpy[i - minutes]

        max_unsat_cust = max(max_unsat_cust, curr_unsat_cust)

    for j in range(len(customers)):
        sat_cust += customers[j] * (1 - grumpy[j])
    
    max_sat_cust = max_unsat_cust + sat_cust
    return max_sat_cust


def main():
    customers, grumpy, mins = [4, 10, 10], [1, 1, 0], 2
    result = max_satisfied(customers, grumpy, mins)
    print("\n" +str(result))

if __name__ == "__main__":
    main()