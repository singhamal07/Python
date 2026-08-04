from typing import List
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)
        order = sorted(range(n), key=lambda i: aliceValues[i] + bobValues[i], reverse=True)
        alice_score = bob_score = 0
        for turn, i in enumerate(order):
            if turn % 2 == 0:
                alice_score += aliceValues[i]
            else:
                bob_score += bobValues[i]
        if alice_score > bob_score:
            return 1
        elif alice_score < bob_score:
            return -1
        else:
            return 0