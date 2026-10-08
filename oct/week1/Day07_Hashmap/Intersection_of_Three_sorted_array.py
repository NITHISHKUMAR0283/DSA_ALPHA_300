class Solution:
    def commonElements(self, a, b, c):
        # code here
        intersection = []
        i = 0
        j = 0
        k = 0
        len1 = len(a)
        len2 = len(b)
        len3 = len(c)
        while i<len1:
            
            ele1 = a[i]
            #treating this as base and increase other pointer if it is less than the current ele 
            #after incrementing other pointers , we check every pointer value are same , if so add to the result 
            
            while j<len2 and  b[j]<ele1:
                j+=1
            while k<len3 and c[k]<ele1:
                k+=1
            if j<len2 and ele1==b[j] and k<len3 and  b[j]==c[k]:
                intersection.append(ele1)
            i+=1
            while i<len1 and i>0 and a[i-1]==a[i]:
                i+=1
            
        return intersection
                