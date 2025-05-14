def is_palindrome(s):
    # Keep only alphanumeric characters and convert to lowercase
    filtered = "".join(char.lower() for char in s if char.isalnum())
    # Check if the filtered string is the same forwards and backwards
    return filtered == filtered[::-1]


# Example usage:
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))
