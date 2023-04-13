def biggestPalindrome(self, s: str) -> str:
        biggest = ''
        def find(s, l, r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        
        for i in range(len(s)):
            s1 = find(s, i, i)
            if len(s1) > len(biggest): biggest = s1
            
            s2 = find(s, i, i+1)
            if len(s2) > len(biggest): biggest = s2
                
        return biggest