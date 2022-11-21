class Solution:
   def solve(self, number):
      s=''
      sign = '-' if number<0 else ''
      number= abs(number)
      if number < 3:
         return str(number)
      while number != 0:
         s = str(number%3) + s
         number = number//3
      return sign+s
ob = Solution()
num=int(input())
print(ob.solve(num))


