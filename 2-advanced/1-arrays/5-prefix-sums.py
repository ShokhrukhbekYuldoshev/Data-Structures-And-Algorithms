# https://leetcode.com/problems/range-sum-query-immutable/
# https://leetcode.com/problems/range-sum-query-2d-immutable/
# https://leetcode.com/problems/find-pivot-index/
# https://leetcode.com/problems/product-of-array-except-self/
# https://leetcode.com/problems/subarray-sum-equals-k/

class PrefixSum:

    def __init__(self, nums):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)
        
    def rangeSum(self, left, right):
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 0 else 0
        return (preRight - preLeft)