# https://leetcode.com/problems/permutations/


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        permutations = [[nums[0]]]

        for i in range(1, len(nums)):
            permutations = [
                [*p[:j], nums[i], *p[j:]]
                for j in range(i + 1)
                for p in permutations
            ]
        
        return permutations
