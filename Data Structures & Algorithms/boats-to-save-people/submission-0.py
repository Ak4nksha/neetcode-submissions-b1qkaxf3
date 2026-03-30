class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        n = len(people)
        i = 0
        j = n-1
        cnt = 0
        people = sorted(people)

        while i<=j:

            if people[i] + people[j] <= limit:

                cnt += 1
                i += 1
                j -= 1

            else:
                cnt += 1
                j -= 1

        return cnt

