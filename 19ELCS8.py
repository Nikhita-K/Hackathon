class Solution:
  def longestPalindrome(self, s: str) -> str:
    # @ and $ signs are sentinels appended to each end to avoid bounds checking
    t = '#'.join('@' + s + '$')
    n = len(t)
    # t[i - mE[i]..i) ==
    # t[i + 1..i + mE[i]]
    mE = [0] * n
    center = 0

    for i in range(1, n - 1):
      rightBoundary = center + mE[center]
      mirrorIndex = center - (i - center)
      mE[i] = rightBoundary > i and \
          min(rightBoundary - i, mE[mirrorIndex])

      # Attempt to expand palindrome centered at i
      while t[i + 1 + mE[i]] == t[i - 1 - maxE[i]]:
        mE[i] += 1

      # If palindrome centered at i expand past rightBoundary,
      # adjust center based on expanded palindrome.
      if i + mE[i] > rightBoundary:
        center = i

    # Find the maxExtend and bestCenter
    maxExtend, bestCenter = max((extend, i)
                                for i, extend in enumerate(mE))
    return s[(bestCenter - maxExtend) // 2:(bestCenter + maxExtend) // 2]
