def is_palindrome_valid(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():  # Skip non-alphanumeric chars
            left += 1
        while left < right and not s[right].isalnum():  # Skip non-alphanumeric chars
            right -= 1
        if s[left].lower() != s[right].lower():  # Compare characters (case-insensitive)
            return False
        left += 1
        right -= 1
    return True
