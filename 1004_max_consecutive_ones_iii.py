# https://leetcode.com/problems/max-consecutive-ones-iii/


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # Решение через скользящее окно. Нужно сдвигать на каждом шаге правую
        # границу. Если после сдвига правой границы кол-во "0" в подстроке
        # превышает "k", то нужно сдвигать левую границу, до тех пор пока
        # кол-во "0" снова не станет k. Пересчитать max_length.

        max_length, left, zeros_count = 0, 0, 0

        for right, num in enumerate(nums):
            
            if num == 0:
                zeros_count += 1

                while zeros_count > k:
                    if nums[left] == 0:
                        zeros_count -= 1
                    left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
