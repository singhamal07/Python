def longest_uniform_substring_after_replacements(s: str, k: int) -> int:
    max_len = 0
    for target_char in set(s):
        left = 0
        count_diff = 0
        for right in range(len(s)):
            if s[right] != target_char:
                count_diff += 1
            while count_diff > k:
                if s[left] != target_char:
                    count_diff -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
    return max_len
