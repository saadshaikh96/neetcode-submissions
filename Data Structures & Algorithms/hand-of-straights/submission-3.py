class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize > 0:
            return False

        count = {}
        for num in hand:
            count[num] = count.get(num, 0) + 1

        hand.sort()
        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize):
                    if i not in count or count[i] == 0:
                        return False
                    count[i] -= 1
        return True