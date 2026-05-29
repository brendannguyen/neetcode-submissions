class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        
        return encoded_string

        # O(n) where n is number of strings

    def decode(self, s: str) -> List[str]:
        strs = []
        
        i = 0
        while i < len(s):
            # gets string length (up to #)
            str_len = ""
            for j in range(i, len(s)):
                if s[j] == "#":
                    break
                str_len += s[j]

            str_len = int(str_len)

            # sets i to j + 1 (start of new string)
            i = j+1

            # slices string
            strs.append(s[i:i+str_len])

            # sets i to start of next sequence
            i += str_len
            
        return strs

        # O(k) where k is number of characters in encoded string


        # Overall O(k)
