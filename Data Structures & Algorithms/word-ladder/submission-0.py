class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        words = set(wordList)
        q = deque()
        q.append((beginWord, 1))
        # print(q)
        if beginWord in words:
            words.remove(beginWord)
        if beginWord == endWord: return 1

        while q:
            # print(q)
            word, seq = q.popleft()
            if word == endWord:
                return seq
            
            for i in range(len(word)):
                for j in range(26):
                    char = chr(j + ord('a'))
                    s1 = word[: i] + char + word[i+1:]
                    # print(s1)

                    if s1 in words:
                        words.remove(s1)
                        q.append((s1,seq+1))


        return 0



                









