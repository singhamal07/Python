class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        cleaned = s.replace("-", "").upper()
        first = len(cleaned) % k
        groups = []
        if first:
            groups.append(cleaned[:first])
        for i in range(first, len(cleaned), k):
            groups.append(cleaned[i:i+k])
        return "-".join(groups)
