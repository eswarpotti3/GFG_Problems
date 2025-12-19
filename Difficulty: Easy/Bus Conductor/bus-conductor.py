class Solution:
    def findMoves(self, chairs, passengers):
        # code here
        chairs.sort()
        passengers.sort()
        sum=0
        for i in range(len(chairs)):
            sum+=abs(passengers[i]-chairs[i])
        return sum
