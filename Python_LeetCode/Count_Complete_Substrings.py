class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        
        def count_in_segment(seg: str) -> int:
            total = 0
            n = len(seg)

            # Try every possible number of distinct characters (1 to 26)
            for m in range(1, 27):
                win_size = m * k
                if win_size > n:
                    break

                freq = {}
                # Tracks how many characters have exactly k occurrences
                exact_k = 0

                # Initialize the first window
                for i in range(win_size):
                    ch = seg[i]
                    freq[ch] = freq.get(ch, 0) + 1
                    if freq[ch] == k:
                        exact_k += 1
                    elif freq[ch] == k + 1:
                        exact_k -= 1

                # A window is complete if all m distinct chars appear exactly k times
                if exact_k == m and len(freq) == m:
                    total += 1

                # Slide the window
                for i in range(win_size, n):
                    # Add new right character
                    right = seg[i]
                    freq[right] = freq.get(right, 0) + 1
                    if freq[right] == k:
                        exact_k += 1
                    elif freq[right] == k + 1:
                        exact_k -= 1

                    # Remove old left character
                    left = seg[i - win_size]
                    if freq[left] == k:
                        exact_k -= 1
                    elif freq[left] == k + 1:
                        exact_k += 1
                    freq[left] -= 1
                    if freq[left] == 0:
                        del freq[left]

                    if exact_k == m and len(freq) == m:
                        total += 1

            return total

        # Split word into segments where adjacent chars differ by at most 2
        result = 0
        start = 0
        for i in range(1, len(word)):
            if abs(ord(word[i]) - ord(word[i - 1])) > 2:
                result += count_in_segment(word[start:i])
                start = i
        result += count_in_segment(word[start:])

        return result
