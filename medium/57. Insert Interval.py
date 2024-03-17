from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        if intervals == []:
            res.append(newInterval)

        for i, [start, end] in enumerate(intervals):
            if end < newInterval[0]:
                res.append([start, end])
                if i == len(intervals)-1 or intervals[i+1][0] > newInterval[1]:
                    res.append(newInterval)
            else: 
                if start > newInterval[1]:
                    if res == []:
                        res.append(newInterval)
                    res.append([start, end])
                else:
                    newInterval[0] = min(start, newInterval[0])
                    newInterval[1] = max(end, newInterval[1])
                    if i == len(intervals)-1:
                        res.append(newInterval)
                    elif intervals[i+1][0] > newInterval[1]:
                        res.append(newInterval)
        return res