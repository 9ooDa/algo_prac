class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        ans = True
        temp = []
        while hand:
            if len(temp) == groupSize:
                temp = []

            hand.sort()

            if not temp:
                temp.append(hand.pop(0))
            else:
                if temp[-1] + 1 in hand:
                    nxt = temp[-1] + 1
                    temp.append(nxt)
                    hand.remove(nxt)
                else:
                    ans = False
                    break

        return ans