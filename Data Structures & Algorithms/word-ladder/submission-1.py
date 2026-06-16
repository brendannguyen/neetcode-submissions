class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        queue = deque([beginWord])
        words = set(wordList)

        output = 0
        while queue:
            output += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == endWord:
                    return output

                # replace each cahr with each 26 char (skip same characters), and check in wordList
                for i in range(len(cur)):
                    for c in range(97, 123):
                        if chr(c) == cur[i]:
                            continue
                        
                        new = cur[:i] + chr(c) + cur[i+1:]
                        if new in words:
                            queue.append(new)
                            words.remove(new)
                

                

        return 0