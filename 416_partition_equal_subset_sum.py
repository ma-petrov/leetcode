# https://leetcode.com/problems/partition-equal-subset-sum/


class Solution:
    def canPartition(self, nums: list[int]) -> bool:

        # Если сумма элемементов массива нечетная, то разбить нельзя.
        if (total_sum := sum(nums)) & 1:
            return False

        subset_sum = total_sum // 2

        # i-ый элемент - флаг, можно ли составить подмассив с суммой, равной i.
        can_partition = [True] + [False] * subset_sum

        # Для каждого числа в массиве проверяется, можно ли составить с ним
        # подмассив суммы s.
        for num in nums:

            # Суммы нужно перепибирать в обратном порядке. Например для массива
            # [1, 3] can_partition будет равен [T, F, F, F, F]. Если идти с
            # начала, на первой итерации при num == 1 переменная s будет равна
            # 1, что по условию can_partition[s] даст True, после этого шага
            # can_partition будет в следующем состоянии - [T, T, F, F, F], на
            # второй итерации при num == 1, s == 2 can_partition[s - num] 
            # вернет True, что некорректно, потому что num использует самого
            # себя в условии can_partition[s - num]. Поэтому нужно
            # итерироваться с конца, тогда условие can_partition[s] сработает
            # в последний момент.
            for s in range(subset_sum, num - 1, -1):

                # Можно составить подмассив с суммой равной s либо из одного
                # числа, которое равно s, либо если уже определено, что для
                # суммы s - num можно составить подмассив, тогда s - num + num
                # дадут в сумме s.
                can_partition[s] = can_partition[s] or can_partition[s - num]

        return can_partition[subset_sum]
