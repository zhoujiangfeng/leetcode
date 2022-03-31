class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 :
            return False
        x = list(map(int,str(x)))
        for i in range(int(len(x)/2)):
            if x[i]!=x[len(x)-1-i]:

                print("false")
                return False
        else:
            print("true")
            return True
if __name__ == '__main__':

    Solution().isPalindrome(x=-111)