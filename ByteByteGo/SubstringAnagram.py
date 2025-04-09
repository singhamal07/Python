from collections import Counter

def substring_anagrams(s: str, t: str) -> int:
    len_t = len(t)
    len_s = len(s)

    if len_t == 0 or len_t > len_s:
        return 0

    t_counter = Counter(t)
    window_counter = Counter(s[:len_t])
    count = 0

    if window_counter == t_counter:
        count += 1

    for i in range(len_t, len_s):
        left_char = s[i - len_t]
        right_char = s[i]

        window_counter[left_char] -= 1
        if window_counter[left_char] == 0:
            del window_counter[left_char]

        window_counter[right_char] += 1

        if window_counter == t_counter:
            count += 1

    return count
