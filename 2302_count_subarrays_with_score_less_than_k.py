# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/description/


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        # Для каждого right всевозможные варианты подмассивов:
        # с [0 : right + 1] по [right : right + 1]. В совокупности это все
        # варианты подмассивов в массиве nums.
        # 
        # Если для некоторого right0 существует такой left0, при котором 
        # подмассив [left0 : right0 + 1] удовлетворяет условию, то для всех
        # leftN, таких что left0 <= leftN <= right1, подмассивы 
        # [leftN : right0 + 1] будут удовлетворять словию, так как их сумма и
        # длина будут меньше и, соответственно, произведение суммы на длину,
        # будет меньше, чем у подмассива [left0 : right0 + 1].
        #
        # Таким же образом доказывается обратный случай, когда подмассивы не
        # удовлетворяют условию.
        #
        # В решении для каждого right нужно найти такой left, чтобы подмассив
        # удовлетворял условию. Тогда для каждого right кол-во удовлетворящих
        # условию подмассивов count == right - left + 1. Для конечного ответа
        # нужно просуммировать все count. Сумма эл-во подмассива subarray_sum
        # вычисляется кумулятивно на каждом шаге.

        subarrays_count = left = subarray_sum = 0

        for right in range(len(nums)):

            # На каждом шаге с новым right увеличивается сумма.
            subarray_sum += nums[right]

            # Поиск left, при котором подмассив станет удовлетворять условию,
            # уменьшение суммы subarray_sum по мере исключения элементов слева.
            while left <= right and subarray_sum * (right - left + 1) >= k:
                subarray_sum -= nums[left]
                left += 1
            
            # Добавление кол-ва эподмассивов для i-го right, удовлетворяющих
            # условию, в общую сумму.
            subarrays_count += right - left + 1
        
        return subarrays_count
