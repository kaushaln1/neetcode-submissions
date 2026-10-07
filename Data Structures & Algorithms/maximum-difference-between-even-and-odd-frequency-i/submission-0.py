class Solution:
    def maxDifference(self, s: str) -> int:

        hashmap = defaultdict(int)

        for i in s:
            hashmap[i]+=1
        

        max_odd = -1
        min_even = 10000000
        for key,value in hashmap.items():
            print (key , value)
            if value %2 ==0 and value < min_even: 
                min_even = value
            elif value %2 != 0 and value > max_odd:
                max_odd = value
        

        return max_odd - min_even

        