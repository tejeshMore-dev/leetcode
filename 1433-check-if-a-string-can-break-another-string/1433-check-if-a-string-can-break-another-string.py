class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        N = len(s1)

        x = sorted(s1)
        y = sorted(s2)
        can_break = False

        can_break = all( x[i] >= y[i] for i in range(N) )
        can_break = all( y[i] >= x[i] for i in range(N) ) or can_break

        return can_break
        