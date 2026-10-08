class Solution(object):
    def isPalindrome(self, x):
        rev= 0
        copy = x
        num = []
        # % will give the last digit and / will remove the last digit , so we can get last digit with these two operators , we store in list and do it again and compare with list 
        if copy<0:
            return False
        while copy!=0:
            num.append(copy%10)
            copy/=10
        copy = x
        right = len(num)-1
        while right>=0:
            if copy%10!=num[right]:
                return False
            copy/=10
            right-=1
        return True
        