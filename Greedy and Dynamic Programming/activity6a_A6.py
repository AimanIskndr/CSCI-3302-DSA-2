import random

memo = [[], [], []]

# Test cases: includes given lists and randomly generated lists
test_cases = [
    # Given test case lists
    [21, 18, 4, 13, 9, 16, 2, 23, 6, 11, 17, 22, 8, 19, 14],  # mcoinrow1.txt  
    [21, 18, 4, 13, 9, 16, 2, 23, 6, 11, 17, 22, 8, 19, 14, 20, 5, 12, 7, 3, 25, 24, 10, 1, 15, 22, 9, 17, 14, 3],  # mcoinrow2.txt
    # Randomly generated test case
    [],  # Placeholder for 50 randomly generated integers
    []   # Placeholder for 100 randomly generated integers
]

# Generate 50 random integers (values: 1 ~ 25) and add to test_cases list
for i in range(50):
    test_cases[2].append(random.randint(1, 25))
    
# Generate 100 random integers (values: 1 ~ 25) and add to test_cases list
for i in range(100):
    test_cases[3].append(random.randint(1, 25))

# Recursive function to compute the maximum sum from coins
def F(n):
    if n < 0:  # Base case: if index is out of bounds, return 0
        return 0
    if memo[2][n]:  # If the result for the current index is already computed, just return it
        return memo[2][n]

    best = max(memo[1][n] + F(n-3), F(n-2), F(n-1))
    memo[2][n] = best
    
    return memo[2][n]

# Function to find all the index of the picked coin
def find_picked_index(cur_sum, id):
    indexes = []
    while cur_sum != 0 and id > 0:
        
        if memo[2][id] - memo[1][id] == memo[2][max(id-3,0)]:
            indexes.append(id)
            cur_sum -= memo[1][id]
            id -= 2 # skip 2 if we take the index
            
        id -= 1
    
    indexes.sort()  # Sort the indexes in ascending order
    return indexes

# Iterate through each test case and print the maximum sum
for tc in test_cases:
    
    for row in memo: # clear the memo table and add column 0
        row.clear()
        row.append(0)

    for i, c in enumerate(tc, 1):
        memo[0].append(i) # table index row
        memo[1].append(c) # coin value row
        memo[2].append(0) # best sum row
    
    n = len(tc)
    best_sum = F(n) # Call the recursive function with starting index 0 and the current test case
    
    # print max value obtain
    print("\nMaximum possible sum of coins: " + str(best_sum) + "\n")
    
    # print the memo table
    print("i: ", end='')
    print('\t'.join(str(x) for x in memo[0])) # table index row
    
    print("c: ", end='')
    print('\t'.join(str(x) for x in memo[1])) # coin value row
    
    print("F: ", end='')
    print('\t'.join(str(x) for x in memo[2])) # best sum row
    
    # print index of each chosen coin & value of each chosen coin
    picked_indexes = find_picked_index(best_sum, n)
    print("Picked Index: " + str(picked_indexes))
    
    picked_coins = [memo[1][i] for i in picked_indexes]
    print("Picked Coins: " + str(picked_coins))
