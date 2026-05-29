class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create a list
        # add first str to firet inner list
        # for each next str, compare eith first str of rwch inner list
        # if same, add to inner list
        # add to own inner list

        anagrams = []

        for word in strs:
            found = False
            for group in anagrams:
                if sorted(word) == sorted(group[0]):
                    found = True
                    group.append(word)
                    break
            
            if not found:
                anagrams.append([word])

        return anagrams
