class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        all_map = {}
        for s in strs:
            key = tuple(sorted(s))  # sorted tuple as key
            if key in all_map:
                all_map[key].append(s)
            else:
                all_map[key] = [s]

        return list(all_map.values())




                
        