class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        mid = len(nums)//2
        if nums[mid] == target:
            return mid
        if target > nums[mid]:
            nums = nums[mid+1:]
            res = self.search(nums,target)
            return mid+1+res if res != -1 else -1
        if target < nums[mid]:
            nums = nums[0:mid]
            return self.search(nums,target)
        return -1