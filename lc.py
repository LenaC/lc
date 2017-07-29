import os


class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0 : return '-'+self.convertToBase7(-num)
        if num < 7 : return str(num)
        return self.convertToBase7(num//7) + str(num%7)

    def test_convertToBase7(self):
    	"""test harness"""
    	assert(self.convertToBase7(100) == "202")
    	assert(self.convertToBase7(-7) == "-10")


os.system("clear")
print("-" * 80)
print("i love leet!")
print("-" * 80)


sol = Solution()
sol.test_convertToBase7()