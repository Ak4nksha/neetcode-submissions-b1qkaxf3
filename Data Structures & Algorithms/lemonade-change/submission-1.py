class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        

        n = len(bills)
        five, ten = 0, 0

        for i in bills:

            if i == 5:

                five += 1
            
            elif i == 10 and five > 0:
                 
                 five -= 1
                 ten += 1

            elif five > 0 and i == 20:

                if ten > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False

            else:
                return False

        return True

