class Solution(object):
    def videoStitching(self, clips, time):
        # sort clips
        clips.sort(key=lambda x: x[0])
        current_end, farthest_end, count = 0,0,0
        i = 0
        while current_end < time: # find the farthest reach in current interval
            while i < len(clips) and clips[i][0] <= current_end:
                farthest_end = max(farthest_end, clips[i][1])
                i+=1

            if current_end == farthest_end:
                return -1
            
            current_end = farthest_end # update current to the farthest
            count += 1
        
        return count
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
