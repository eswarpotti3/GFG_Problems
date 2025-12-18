class Solution:
    def minJumps(self, arr):
        if len(arr) == 1:
            return 0
        if arr[0] == 0:
            return -1
        
        jumps = 0
        current_max = 0
        next_max = 0
        
        for i in range(len(arr) - 1):
            next_max = max(next_max, i + arr[i])
            
            if i == current_max:
                jumps += 1
                current_max = next_max
                
                if current_max >= len(arr) - 1:
                    break
        
        if current_max < len(arr) - 1:
            return -1
        
        return jumps