def make_ends(nums):
  if len(nums)<0:
    return nums
  else:
    a=[]
    a.append(nums[0])
    a.append(nums[-1])
    return a
