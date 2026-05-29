class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs = []
        
        i = 0
        while i < len(s):
            str_len = ""
            for j in range(i, len(s)):
                if s[j] == "#":
                    break
                str_len += s[j]

            str_len = int(str_len)
            i = j+1

            strs.append(s[i:i+str_len])
            i += str_len
            
        
        return strs