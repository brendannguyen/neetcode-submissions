class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        positions = {}
        output = []
        
        for i in range(len(s)):
            positions[s[i]] = max(positions.get(s[i], 0), i)
        
        size = 0
        end = 0
        for i in range(len(s)):
            end = max(end, positions[s[i]])
            size += 1

            if i == end:
                output.append(size)
                size = 0
        
        return output

