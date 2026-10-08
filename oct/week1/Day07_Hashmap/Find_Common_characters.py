class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        freq = {}
        #Build a freq of first word
        for char in words[0]:
            if char not in freq:
                freq[char]=0
            freq[char]+=1
        #for each word build freq and take common key with its minimum value among existing freq and current freq and make that as the running freq
        for word in words:
            curr_freq = {}
            for char in word:
                if char not in curr_freq:
                    curr_freq[char]=0
                curr_freq[char]+=1
            intersection = {}
            for key,value in freq.items():
                if key in curr_freq:
                    intersection[key]=min(value,curr_freq[key])
            freq = intersection.copy()
        commonChar = []
        # converstion of dictionary to list
        for key,value in freq.items():
            for _ in range(value):
                commonChar.append(key)
        return commonChar


