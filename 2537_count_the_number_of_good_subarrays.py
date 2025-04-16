# https://leetcode.com/problems/count-the-number-of-good-subarrays/


import collections


class Solution:
    def countGood(self, nums: list[int], k: int) -> int:

        good_count, pairs_count, r = 0, 0, 1
        nums_count = collections.defaultdict(int)
        nums_count[nums[0]] = 1

        # Для каждого l нужно такой минимальный r так, чтобы отрезок
        # l:r удовлетворял условию
        for l in range(len(nums) - 1):

            # Для кажддого l всегда поиск начинается с предыдущего r, 
            # так как если l2 > l1 и для l1 условие выполняется при r > r1,
            # то для l2 условие выполнится при r > r2 >= r1.
            while r < len(nums) and pairs_count < k:
                
                nums_count[nums[r]] += 1
                pairs_count += nums_count[nums[r]] - 1
                r += 1
            
            # Кол-во отрезков для l равно len(nums) - r + 1
            if pairs_count >= k:
                good_count += len(nums) - r + 1
            
            # Если отрезок l:r не удовлетворяет условию, а r == len(nums),
            # значит больше нельзя найти отрезки удовлетворяющие условию.
            elif r == len(nums):
                break

            # На следующем шаге l увеличится на 1 и элемент nums[l] нужно
            # убрать из расчета
            pairs_count -= nums_count[nums[l]] - 1
            nums_count[nums[l]] -= 1
        
        return good_count
