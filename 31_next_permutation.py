# https://leetcode.com/problems/next-permutation/


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        length = len(nums)
        
        # Поиск невозрастающей последовательности [pivot + 1, len(nums)]
        pivot = -1
        for i in range(length - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
        
        # Если все число - невозрастающая последовательность, значит это
        # максимальное число. Следующее число будет минимальное, нужно все
        # число переписать в обратном порядке.
        if pivot == -1:
            nums.reverse()
            return

        # Иначе нужно заменить pivot "следующей" цифрой по возрастанию, а
        # оставашиеся цифры, включая pivot развренуть.
        for j in range(length - 1, pivot, -1):
            if nums[j] > nums[pivot]:
                nums[pivot], nums[j] = nums[j], nums[pivot]
                break

        nums[pivot + 1:] = reversed(nums[pivot + 1:])


nums = [2, 4, 3, 2, 1]
Solution().nextPermutation(nums)
print(nums)
