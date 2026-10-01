class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss=[]
        for char in s:
            if char.isalnum():
                ss.append(char.lower())


        i =0
        j = len(ss)-1
        while i<j:
            if ss[i] == ss[j]:
                i+=1
                j-=1
            else:
                return False
        return True

        # map = {}
        # for char in ss:
        #     if char in map:
        #         map[char]+=1
        #     else:
        #         map[char] =1 

        # count =0
        # for val in map.values():
        #     if val %2 != 0:
        #         count+=1
        
        # if count >1 :
        #      return False
        # return True



        