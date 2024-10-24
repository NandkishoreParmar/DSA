
# 1 st way 


def detect_palindrome(num):
    res = num
    ans = 0

    while res > 0:
        x = res % 10
        res //= 10  # Integer division to remove the last digit
        ans = ans * 10 + x  # Reversing the number

    if ans == num:
        print("Yes, it's a palindrome")
    else:
        print("No, it's not a palindrome")


# Time Complexity: O(d)=O(log10(num))
# The time complexity of the detect_palindrome function depends on the number of digits in the input number num.

# While Loop: The loop runs once for each digit in the number num. If the number has d digits, the loop will execute d times.

# Extracting the last digit using res % 10 and removing it using res //= 10 are constant-time operations, so the overall cost per iteration is O(1).
# The number of digits d in a number num is proportional to log10(num), since there are approximately log10(num) digits in a number num.

# Thus, the time complexity is:   O(d)=O(log10(num))

# Space Complexity: O(1)
# The function uses a constant amount of space regardless of the size of the input num.
# Variables res, ans, and x all take constant space.
# There are no additional data structures or recursive calls, so the space complexity is: O(1)

# 2nd way string check
def detect_palindrome(num):
    num_str = str(num)  # Convert the number to a string
    left = 0  # Left pointer starts at the beginning of the string
    right = len(num_str) - 1  # Right pointer starts at the end of the string

    # Move the two pointers towards the center
    while left < right:
        if num_str[left] != num_str[right]:
            print("No, it's not a palindrome")
            return  # Exit early if mismatch is found
        left += 1
        right -= 1

    # If the loop completes, the number is a palindrome
    print("Yes, it's a palindrome")


# Time Complexity:O(log10(num))).
# String Conversion: Converting the number to a string takes O(d), where d is the number of digits in the number (or O(log10(num))).
# Two Pointer Comparison: The two-pointer loop iterates d/2 times, which is O(d).
# Space Complexity:O(log10(num))).
# The space complexity is O(d) due to the string representation of the number.
# Thus, the space complexity is: O(log10(num))).

# 3 rd way 

def detect_palindrome(s):
    left = 0  # Left pointer starts at the beginning of the string
    right = len(s) - 1  # Right pointer starts at the end of the string

    # Move the two pointers towards the center
    while left < right:
        if s[left] != s[right]:
            print("No, it's not a palindrome")
            return  # Exit early if mismatch is found
        left += 1
        right -= 1

    # If the loop completes, the string is a palindrome
    print("Yes, it's a palindrome")

# Test with the string "madam"
detect_palindrome("madam")  # Output: Yes, it's a palindrome

# Time and Space Complexity:
# Time Complexity: O(n) where n is the length of the string.
# Space Complexity: O(1) since we only use two pointers and no extra data structures.