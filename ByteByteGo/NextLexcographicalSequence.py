def next_lexicographical_sequence(s: str) -> str:
    chars = list(s)
    i = len(chars) - 2
    while i >= 0 and chars[i] >= chars[i + 1]:
        i -= 1
    if i == -1:
        return "".join(sorted(chars))
    j = len(chars) - 1
    while chars[j] <= chars[i]:
        j -= 1
    chars[i], chars[j] = chars[j], chars[i]
    chars[i + 1:] = reversed(chars[i + 1:])
    return "".join(chars)
