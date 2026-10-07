class Solution:    
    def findUnion(self, a, b):
        # code here
        seen = set()
        #just add the unique element of both array and convert set to list
        for ele in a:
            seen.add(ele)
        for ele in b:
            seen.add(ele)
        Union = [] 
        for ele in seen:
            Union.append(ele)
        return Union