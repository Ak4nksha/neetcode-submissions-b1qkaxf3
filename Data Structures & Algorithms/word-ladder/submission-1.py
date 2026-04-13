class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0

        nei = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)

        q = deque([(beginWord, 1)])
        visit = set([beginWord])

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps

            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]

                for neiWord in nei[pattern]:
                    if neiWord not in visit:
                        visit.add(neiWord)
                        q.append((neiWord, steps + 1))

        return 0



                









