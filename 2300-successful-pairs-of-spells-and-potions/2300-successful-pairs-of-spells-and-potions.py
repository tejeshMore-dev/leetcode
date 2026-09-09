class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)

        def count(spell: int) -> int:
            l = 0
            r = len(potions)
            target = ceil(success / spell)

            while l < r:
                mid = l + (r - l) // 2

                if target <= potions[mid]:
                    r = mid
                else:
                    l = mid + 1
                            
            return n - l
        
        ans = []
        for spell in spells:
            ans.append(count(spell))
        
        return ans