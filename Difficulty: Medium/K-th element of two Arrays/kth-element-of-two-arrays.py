class Solution:
    def kthElement(self, a, b, k):
        count=0  # Start from 0
        i=j=0
        lena=len(a)
        lenb=len(b)
        last = -1  # Track last selected
        
        while i<lena and j<lenb:
            if a[i]<b[j]:
                last = a[i]
                i+=1
            else:
                last = b[j]
                j+=1
            count+=1
            if count==k:
                return last
        # Rest remains same but use 'last'
        while i<lena and count<k:
            last = a[i]
            i+=1
            count+=1
        while j<lenb and count<k:
            last = b[j]
            j+=1
            count+=1
        return last
