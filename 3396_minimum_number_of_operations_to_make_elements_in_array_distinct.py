# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/


class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        # Так как можно удалять только с начала, с конца не должно быть
        # одинаковых чисел. Как только с конца найдено повторяющееся число,
        # до него включая нужно удалить все.
        
        seen = set()
        for index in range(len(nums) - 1,  -1, -1):
            if nums[index] in seen:
                return index // 3 + 1
            seen.add(nums[index])
        return 0
