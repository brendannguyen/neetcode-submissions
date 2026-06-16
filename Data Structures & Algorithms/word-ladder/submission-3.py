class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS, O(m^2 * n) where m is length of word, n is num of words
        # by instead of precomputating neighbour words, create new words by replacing with 26 chars
        # check if this newly created word is in word list (set), if so add to bfs queue, and remove from word list so it is not repeated
        queue = deque([beginWord])
        words = set(wordList)

        output = 0
        while queue:
            output += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == endWord:
                    return output

                # replace each char with each 26 char (skip same characters), and check in wordList
                for i in range(len(cur)):
                    for c in range(97, 123):
                        if chr(c) == cur[i]:
                            continue
                        
                        new = cur[:i] + chr(c) + cur[i+1:]
                        if new in words:
                            queue.append(new)
                            words.remove(new)
                
        return 0