class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set([n])
        ans = True

        while n != 1:
            num = n
            new_n = 0

            while num:
                val = num % 10
                new_n += val * val

                num = num // 10

            if new_n in seen:
                ans = False
                break

            seen.add(new_n)
            n = new_n

        return ans 