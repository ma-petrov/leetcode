# https://leetcode.com/problems/count-complete-subarrays-in-an-array/


class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:

        # Нахождение первого отрезка, в котором будут все числа из массива,
        # а также подсчет кол-ва элементов в отрезке.
        left, right, unique_nums = 0, 0, set(nums)
        nums_count = {num: 0 for num in unique_nums}
        while unique_nums:
            unique_nums.discard(nums[right])
            nums_count[nums[right]] += 1
            right += 1

        # Кол-во возможных вариантов, где начало подмассива это самый элемент
        # равно разнице длины и right, потому что до right встретились все
        # числа, это первый подмассив. Остальные подмассивы получаются добав-
        # лением под одному элементу.
        count = len(nums) - right + 1

        # Далее нужно убирать левый элемент и если больше в подмассиве нет
        # таких элементов, то нужно искать такой же правый. После того как в
        # подмассиве снова есть все элементы, прибавить кол-во новых вариантов.
        while left < len(nums):
            num = nums[left]
            nums_count[num] -= 1
            left += 1

            # Попытка найти элемент, елси его не хватает, чтобы подмассив 
            # удовлетворял условию.
            while right < len(nums) and nums_count[num] == 0:
                nums_count[nums[right]] += 1
                right += 1

            # Если выполнялся поиск недостающего элемента, right мог выйти за
            # границы массива, при этом элемент мог не найтись.
            if nums_count[num] != 0:
                count += len(nums) - right + 1
            
            # Если элемент не нашелся и right вышел за границу массива, то
            # больше подмассивов удовлетворяющих условию нет.
            elif right == len(nums):
                return count
        
        return count
