class Solution(object):
   def longestPalindrome(self, a):
      dpp = [[False for i in range(len(a))] for i in range(len(a))]
      for i in range(len(a)):
         dpp[i][i] = True
      maxi_length = 1
      start = 0
      for l in range(2,len(a)+1):
         for i in range(len(a)-l+1):
            end = i+l
            if l==2:
               if a[i] == a[end-1]:
                  dpp[i][end-1]=True
                  maxi_length = l
                  start = i
            else:
               if a[i] == a[end-1] and dpp[i+1][end-2]:
                  dpp[i][end-1]=True
                  maxi_length = l
                  start = i
      return a[start:start+maxi_length]
ob1 = Solution()
print(ob1.longestPalindrome("ABBABBC"))