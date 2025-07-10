# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/

import itertools


class Solution:
    def maxFreeTime(self, event_time: int, start_time: list[int], end_time: list[int]) -> int:

        meetings_count = len(start_time)
        max_gap_duration = 0

        # Длительность промежутков между митингами
        gap_durations = [
            end - start
            for end, start in zip(
                itertools.chain(start_time, [event_time]),
                itertools.chain([0], end_time),
            )
        ]
        max_left = list(itertools.accumulate(gap_durations, max))
        max_right = list(reversed(list(itertools.accumulate(reversed(gap_durations), max))))

        for meeting_number, (start, end) in enumerate(zip(start_time, end_time)):
            adjacent_gaps_duration = gap_durations[meeting_number] + gap_durations[meeting_number + 1]
            meeting_duration = end - start

            # Митинг можно передвинуть либо внутри соседних промежутков, либо, если позволяет место, в другие
            # промежутки. Митинг можно передвинуть в другие промежутки при условии, что для него найдется место.
            # Это можно вычислить через max_left и max_right.
            if (
                meeting_number > 0 and max_left[meeting_number - 1] >= meeting_duration
                or meeting_number + 1 < meetings_count and max_right[meeting_number + 2] >= meeting_duration
            ):
                # Если текущий митинг можно передвинуть в другие (не соседние промежутки), тогда образуется промежуток
                # равный по продолжительности двух соседних промежуткав и митинга.
                max_gap_duration = max(max_gap_duration, adjacent_gaps_duration + meeting_duration)
            
            else:
                # Если митинг нельзя передвинуть в другие промежутки, тогда его можно поменять местами только с соседним
                # промежутком, в таком случае продолжительность нового промежутка равна семме длительностей соседних
                # промежутков.
                max_gap_duration = max(max_gap_duration, adjacent_gaps_duration)
        
        return max_gap_duration


print(Solution().maxFreeTime(5, [1, 3], [2, 5]))
