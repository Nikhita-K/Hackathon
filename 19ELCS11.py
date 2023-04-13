class Solution(object):
   def longestPalindrome(self, a):
      dp = [[False for i in range(len(a))] for i in range(len(a))]
      for i in range(len(a)):
         dp[i][i] = True
      max_length = 1
      start = 0
      for l in range(2,len(a)+1):
         for i in range(len(a)-l+1):
            endd = i+l
            if l==2:
               if a[i] == a[endd-1]:
                  dp[i][endd-1]=True
                  max_length = l
                  start = i
            else:
               if a[i] == a[endd-1] and dp[i+1][endd-2]:
                  dp[i][endd-1]=True
                  max_length = l
                  start = i
      return a[start:start+max_length]
ob1 = Solution()
print(ob1.longestPalindrome("ABBABBC"))