# 1 first way -- brute Force
arr = [1, 2, 1, 3, 4]
k = 4
n = len(arr)

# Brute force approach to find subarrays with sum equal to k
for i in range(n):
    for j in range(i, n):
        current_sum = 0
        for l in range(i, j + 1):
            current_sum += arr[l]
        if current_sum == k:
            print(f'Subarray found from index {i} to {j}: {arr[i:j+1]}')
            break  # Exiting the loop once a subarray is found

# Time Complexity: O(n^3)
# The outer loop runs n times.
# The second loop runs n - i times, making it a triangular loop.
# The innermost loop runs j - i + 1 times, making it very inefficient.
# Thus, the time complexity of this approach is: O(n^3)

# Space Complexity:   O(1)
# The space complexity is O(1) since no extra space (other than variables) is used.

# 2 nd way 
arr = [1, 2, 1, 3, 4]
k = 6
n = len(arr)

for i in range(n):
    current_sum = 0
    flag = False
    for j in range(i, n):
        current_sum += arr[j]
        if current_sum == k:
            print(f'Subarray found from index {i} to {j}: {arr[i:j+1]}')
            flag = True
            break
    if flag:
        break

#  Time Complexity: O(n^2)
# The outer loop runs n times.
# The inner loop runs n - i times for each value of i.
# This results in a time complexity of:  O(n^2)  
# Space Complexity:  O(1)
# The space complexity remains O(1) since no extra data structures are used apart from a few variables.


# 3 rd way This sliding window approach is more efficient than the brute force and quadratic methods.
def subarrk(n, k, arr):
    current_sum = 0
    j = 0

    for i in range(n):
        # Add the current element to the sum
        current_sum += arr[i]

        # If current_sum exceeds k, shrink the window from the left
        while current_sum > k and j <= i:
            current_sum -= arr[j]
            j += 1

        # Check if we found a subarray with sum equal to k
        if current_sum == k:
            return True  # Subarray found

    return False  # No subarray found

# Time Complexity: O(n)
# The outer loop runs n times.
# The inner while loop doesn't run more than n times because both i and j move forward.
# Thus, the time complexity is: O(n)
# Space Complexity:O(1) 
# The space complexity is O(1) since the algorithm uses only a few variables (current_sum, i, j).


# 4 forth way  two pointer in same direction 
  
def subarrk(n, k, arr):
    i = 0  # First pointer (start of the subarray)
    j = 0  # Second pointer (end of the subarray)
    current_sum = 0

    while j < n:
        # Add the element at index j to the current_sum
        current_sum += arr[j]

        # If current_sum exceeds k, move the first pointer i to reduce the sum
        while current_sum > k and i <= j:
            current_sum -= arr[i]
            i += 1

        # If we find the sum equals to k, return True
        if current_sum == k:
            return True

        # Move the second pointer (j) to expand the window
        j += 1

    # If no subarray is found, return False
    return False

# Time Complexity: O(n)
# Both i and j pointers move forward at most n times.
# Thus, the time complexity is: O(n)
# Space Complexity: O(1)
# The space complexity is O(1) since no additional space is used beyond a few variables.
# This two-pointer approach efficiently finds a subarray with sum k and works well for problems where the array contains only non-negative numbers.