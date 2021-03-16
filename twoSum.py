def twoSum(nums, target):
    memory = {}
    
    for i in range(len(nums)):
        if nums[i] in memory:
            return [memory[nums[i]], i]
        else:
            memory[target-nums[i]] = i
            
print(twoSum([2,7,11,15], 18))           