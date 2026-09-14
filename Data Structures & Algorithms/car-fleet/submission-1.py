class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionSpeedPairs = [(p, s) for p, s in zip(position, speed)]
        positionSpeedPairs.sort(reverse=True)

        numFleets = 1
        prevTimeToTarget = (target - positionSpeedPairs[0][0]) / positionSpeedPairs[0][1]

        for i in range(1, len(positionSpeedPairs)):
            currentPosition, currentSpeed = positionSpeedPairs[i]
            currentTimeToTarget = (target - currentPosition) / currentSpeed
            if currentTimeToTarget > prevTimeToTarget:
                prevTimeToTarget = currentTimeToTarget
                numFleets += 1

        return numFleets