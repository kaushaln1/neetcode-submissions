class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    # slidign window easy //
        left =0 
        maxlength=0
        mapper = defaultdict(int)
        for right,_ in enumerate(s):
            mapper[s[right]]+=1

            key, value = max(mapper.items(), key=lambda item: item[1])
            
            print(right , left)
            if right-left+1 - value > k:
                mapper[s[left]] -= 1
                left+=1
            maxlength = max(maxlength, right-left+1)

        return maxlength      

