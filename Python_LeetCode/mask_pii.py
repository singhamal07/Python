class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            return self._mask_email(s)
        else:
            return self._mask_phone(s)
    def _mask_email(self, s: str) -> str:
        s = s.lower()
        name, domain = s.split('@')
        masked_name = name[0] + "*****" + name[-1]
        return masked_name + '@' + domain
    def _mask_phone(self, s: str) -> str:
        digits = ''.join(c for c in s if c.isdigit())  
        local = "***-***-" + digits[-4:]
        country_code_len = len(digits) - 10
        if country_code_len == 0:
            return local
        else:
            return '+' + '*' * country_code_len + '-' + local