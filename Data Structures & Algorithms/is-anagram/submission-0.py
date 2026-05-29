class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # set/dict count occurences then compare?
        # or dict, final results must be zero (balanced e.g. +1 -1)
        # or sort each string, then compare char by char?

        # if different lengths -> false
        record = {}

        if len(s) != len(t):
            return False

        for i in range(0, len(s)):
            # + 1 for s
            # -1 for t
            record[s[i]] = record.get(s[i], 0) + 1
            record[t[i]] = record.get(t[i], 0) - 1

        for v in record.values():
            if v != 0:
                return False

        return True