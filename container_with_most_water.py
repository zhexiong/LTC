class Solution:
    # @return an integer
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        maxArea = 0
        while i < j:
            area = (j - i) * min(height[i], height[j])
            maxArea = max(maxArea, area)
            # replace the shorter end.
            if height[i] > height [j]:
                j -= 1
            else:
                i += 1
        return maxArea