from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        counter1 = Counter(s1)
        counter2 = Counter(s2[:len(s1)])

        for i in range(len(s1), len(s2)):
            if counter1 == counter2: return True

            counter2[s2[i]] += 1
            if counter2[s2[i-len(s1)]] == 0:
                del counter2[s2[i-len(s1)]]
            else:
                counter2[s2[i-len(s1)]] -= 1
        return counter1==counter2