class Solution:
    def videoStitching(self, clips: list[list[int]], time: int) -> int:
        N = len(clips)
        
        clips.sort()
        covered = 0
        ans = 0
        farthest = 0
        i = 0

        while covered < time:
            farthest = covered

            while i < N and clips[i][0] <= covered:
                farthest = max(farthest, clips[i][1])
                i += 1
            
            if farthest == covered:
                return -1
            
            ans += 1
            covered = farthest

        return ans


            
            
            



        