class Solution:
  def longestPalindrome(self, s: str) -> str:
    # @ and $ signs are sentinels appended to each end to avoid bounds checking
    t = '#'.join('@' + s + '$')
    n = len(t)
    # t[i - maxExtends[i]..i) ==
    # t[i + 1..i + maxExtends[i]]
    maxExtends = [0] * n
    c = 0

    for i in range(1, n - 1):
      rB = c + maxExtends[c]
      mI = c - (i - c)
      maxExtends[i] = rB > i and \
          min(rB - i, maxExtends[mI])

      # Attempt to expand palindrome ced at i
      while t[i + 1 + maxExtends[i]] == t[i - 1 - maxExtends[i]]:
        maxExtends[i] += 1

      # If palindrome ced at i expand past rB,
      # adjust c based on expanded palindrome.
      if i + maxExtends[i] > rB:
        c = i

    # Find the maxExtend and bestc
    maxExtend, bestc = max((extend, i)
                                for i, extend in enumerate(maxExtends))
    return s[(bestc - maxExtend) // 2:(bestc + maxExtend) // 2]
