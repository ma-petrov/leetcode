class Solution:
    def sortColors(self, nums: list[int]) -> None:
        # next_zero, next_two хранят индексы на правую границу группы 0-ей
        # слева и на левую границу группы 2-ек справа.
        next_zero, next_two, current = -1, len(nums), 0

        # все элементы справа от next_two - "2". Если current == next_two, то
        # после current все элементы "2" и больше нечего сортировать.
        while current < next_two:

            # Если встретился "0", нужно поместить его к группе "0" в конец
            # группы.
            if nums[current] == 0:
                next_zero += 1
                nums[next_zero], nums[current] = nums[current], nums[next_zero]
                current += 1
    
            # Если встретилась "2", нужно поместить её к группе "2" в начало
            # группы.
            elif nums[current] == 2:
                next_two -= 1
                nums[next_two], nums[current] = nums[current], nums[next_two]

            else:
                current += 1
