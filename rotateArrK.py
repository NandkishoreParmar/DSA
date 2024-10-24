def rotateArray(n, arr, k):
    if n == 0:
        return
    
    # Adjust k to prevent unnecessary rotations (if k >= n)
    k = k % n
    if k == 0:
        return
    
    # Temporary array to hold the last k elements
    temp = [0] * k
    tempi = 0
    
    # Copy the last k elements into temp
    for i in range(n - k, n):
        temp[tempi] = arr[i]
        tempi += 1
    
    # Shift the rest of the array to the right by k positions
    for i in range(n - k - 1, -1, -1):
        arr[i + k] = arr[i]
    
    # Move the k elements from temp to the front of the array
    for i in range(k):
        arr[i] = temp[i]
    
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
n = len(arr)
k = 2
rotated_arr = rotateArray(n, arr, k)
print(rotated_arr)  # Output: [4, 5, 1, 2, 3]


# Time Complexity:
# Copying the last k elements into temp: O(k)
# Shifting the remaining n-k elements to the right: O(n-k)
# Restoring the k elements from temp: O(k)
# Thus, the overall time complexity is:O(n)

# Space Complexity: O(k)
# The space complexity is O(k) due to the temporary array temp.



# 2 nd way
# Helper function to reverse a portion of the array
def reverse(arr, i, j):
    while i <= j:
        # Swap elements at indices i and j
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1

# Function to rotate the array by k positions
def rotateArr(n, k, arr):
    if n == 0:
        return
    
    # Adjust k to prevent unnecessary rotations
    k = k % n
    if k == 0:
        return arr  # No rotation needed if k is 0
    
    # Step 1: Reverse the first part (0 to n-k-1)
    reverse(arr, 0, n - k - 1)
    
    # Step 2: Reverse the second part (n-k to n-1)
    reverse(arr, n - k, n - 1)
    
    # Step 3: Reverse the whole array (0 to n-1)
    reverse(arr, 0, n - 1)
    
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
n = len(arr)
k = 2
rotated_arr = rotateArr(n, k, arr)
print(rotated_arr)  # Output: [4, 5, 1, 2, 3]

# Time Complexity:
# Reversing a portion of the array takes O(n) in total because each reversal operation is O(n) and we perform three reversals.
# Thus, the overall time complexity is:O(n)

# Space Complexity:
# The algorithm only uses constant extra space (O(1)), as the reversal is done in place without additional arrays.