class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map= {}
        for i, num in enumerate(numbers):
            diff = target - num 
            if diff in map:
                return [map[diff], i+1]
            else:
                map[num]=i+1

        