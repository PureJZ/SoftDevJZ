def reverse3(nums):
  hi=[]
  for i in range(1, len(nums)+1):
    hi.append(nums[-1*i])
  return hi
