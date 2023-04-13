def largestPalindrome(self, s: str) -> str:
        largest = ''
        def fL(s, l, r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        
        for i in range(len(s)):
            s1 = fL(s, i, i)
            if len(s1) > len(largest): largest = s1
            
            s2 = fL(s, i, i+1)
            if len(s2) > len(largest): largest = s2
                
        return largest