def rotate_left3(nums):
  hi=[]
  for i in range(1,len(nums)):
    hi.append(nums[i])
  hi.append(nums[0])
  return hi
