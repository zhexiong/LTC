# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        count = len(points)
        maxNum = 0
        for i in range(count):
            ratioMap = {}
            duplicate = 0
            localMax = 0
            # ratio of 0 - i with point j has been checked.
            for j in range(i + 1, count):
                # duplicate points will be on any line of point j.
                if points[j].x - points[i].x == 0 and points[j].y - points[i].y == 0:
                    duplicate += 1
                    continue
                elif points[j].x - points[i].x != 0:
                    k = float(points[j].y - points[i].y) / (points[j].x - points[i].x)
                else:
                    k = 2 ** 31 - 1
                if k in ratioMap:
                    ratioMap[k] += 1
                else:
                    ratioMap[k] = 1
                if ratioMap[k] > localMax:
                    localMax = ratioMap[k]
            if localMax + duplicate + 1 > maxNum:
                maxNum = localMax + duplicate + 1
        return maxNum