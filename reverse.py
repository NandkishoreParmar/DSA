# // 1 way 

arr = [1, 3, 2, 4, 5]
n = len(arr)
rev = [0] * n  # Initialize 'rev' with n zeros
ind = 0
# print(rev)
for i in range(n-1, -1, -1):  # Loop from n-1 down to 0
    rev[ind] = arr[i]
    ind += 1

print("Original array:", arr)
print("Reversed array:", rev)

# 2 way
rev1 = arr[::-1]
print(rev1)
 
# Time Complexity:  O(n)
# Space Complexity: O(n)

# -------------------------------3rd way -----------------------------------

def reverse(arr,n):
    i = 0
    j = n-1
    while i <= j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1
    print('two pointer :', arr)

reverse(arr,n)
# Time Complexity: For each iteration, the pointers move inward by one position, so in total, they move n/2 steps.
# Since each step involves a constant amount of work (swapping two elements), the time complexity is:  O(n)
# Space Complexity: O(1)
# The function only uses a few extra variables: i, j, and temp.
# The original array arr is modified in place, so no additional space is required for a new array.
# Thus, the space complexity is: O(1)



