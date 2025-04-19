# https://leetcode.com/problems/count-the-number-of-fair-pairs/


class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        # Пусть есть x, l, r такие что x < l < r и для каждого i принадлежащего
        # отрезку l:r выполняется условие lower <= nums[x] + i <= upper, а для
        # i не принадлежащего отрезку - не выполняется. Тогда для x2 >= x1 
        # границы l2 <= l1 и r2 <= r1, так
        # как если x1 + r1 == upper, то x2 + r1 >= upper, и если 
        # x1 + l1 == lower, то x2 + l1 >= lower. Значит r2 нужно двигать влево
        # и l2 нужно двигать влево относительно предыдущего интервала. 

        nums.sort()
        fair_pairs_count, l, r = 0, len(nums), len(nums) - 1

        for x in range(len(nums)):

            while l > 1 and nums[x] + nums[l - 1] >= lower:
                l -= 1

            while r > 0 and nums[x] + nums[r] > upper:
                r -= 1
            
            if r <= x:
                break

            if l < len(nums):
                fair_pairs_count += r - max(l - 1, x)

        return fair_pairs_count
