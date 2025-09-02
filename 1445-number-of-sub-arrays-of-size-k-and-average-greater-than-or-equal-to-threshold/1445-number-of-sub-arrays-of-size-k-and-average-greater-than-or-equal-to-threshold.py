class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, th: int) -> int:
        count = 0
        window_sum = sum(nums[:k])
        if window_sum / k >= th:
            count += 1
        for i in range(k, len(nums)):
           window_sum += nums[i] - nums[i - k]
           if window_sum / k >= th:
            count += 1
        return count