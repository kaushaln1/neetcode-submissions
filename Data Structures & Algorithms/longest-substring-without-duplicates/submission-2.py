class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        s= list(s)
        if len(s) == 1:
            return 1
        max= 0
        for i,char in enumerate(s):

            substr=set()
            for j in range(i, len(s)):
                if s[j] not in substr:
                    substr.add(s[j])
                else:
                    break
            print(len(substr))
            max = len(substr)  if len(substr)> max  else max

        return max



        