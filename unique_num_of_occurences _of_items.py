from typing import List

class Solution:
    def uniqueoccur(self,arr: List[int])->bool:
        counts={}
        for item in arr:
            counts[item] = counts.get(item,0)+1

        values= list(counts.values())
        return len(values)==len(set(values))


if __name__ == "__main__":
    arr = [1,1,2,2,3,1,2]
    soln = Solution()
    print(soln.uniqueoccur(arr))