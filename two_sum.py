class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in hashmap:
                return [i, hashmap[rem]]
            else:
                hashmap[nums[i]] = i

#Test Case
obj1 = Solution()
print(obj1.twoSum([3,4,2,3], 6))
print(obj1.twoSum([4,5,7,8], 9))

        