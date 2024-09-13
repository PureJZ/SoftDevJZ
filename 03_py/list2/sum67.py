def sum67(nums):
    total_sum = 0
    flag = False
    index = 0
    
    while index < len(nums):
        if nums[index] == 6:
            flag = True
        elif nums[index] == 7 and flag:
            flag = False
        elif not flag:
            total_sum += nums[index]
        index += 1
        
    return total_sum
