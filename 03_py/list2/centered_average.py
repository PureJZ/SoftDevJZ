def centered_average(nums):
  nums.sort()
  return (sum(nums)-nums[0]-nums[-1])/(len(nums)-2)
