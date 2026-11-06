class Solution(object):
    nums = [3,2,4]
    target = 6



    def two_sum(nums,target):
        for x,a in enumerate(nums):
            soma = target - a
            
            
            for z,nu in enumerate(nums) :
                
                if x != z:
                    
                    if nums[z] == soma:
                        return [z,x]

    a = two_sum(nums,target)
    print(a)
            