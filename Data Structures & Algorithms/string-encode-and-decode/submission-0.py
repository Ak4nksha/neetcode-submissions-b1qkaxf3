class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded = ''
        for ele in strs:
            n = len(ele)
            encoded += str(n) + '#' + ele  

        return encoded      
    def decode(self, s: str) -> List[str]:

        #print(s)
        ans = []
        n = len(s)
        i = 0
        k = ''

        while i < n:
            
            while s[i] != '#':
                k += s[i]
                i += 1
                continue

            if k != '':
                k = int(k)
            
                j = i + k 
                ans.append(s[i+1:j+1])
                i = j + 1
                k = ''
                continue
            else:
                print('some error')
                break

        return ans





