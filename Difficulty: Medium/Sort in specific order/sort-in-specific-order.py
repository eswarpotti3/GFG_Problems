class Solution:
    def sortIt(self, arr):
        i=0
        i=0
        even=[]
        odd=[]
        while i<len(arr):
            if arr[i]%2==0:
                even.append(arr[i])
                
                
            else:
                odd.append(arr[i])
            i+=1
        arr[:]=(sorted(odd,reverse=True)+sorted(even))
        
                
            
