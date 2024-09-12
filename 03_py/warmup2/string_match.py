def string_match(a, b):
  count=0
  if len(a)>=len(b):
    for i in range(len(b)-1):
      if a[i]==b[i] and a[i+1]==b[i+1]:
        count+=1
  else:
    for i in range(len(a)-1):
      if a[i]==b[i] and a[i+1]==b[i+1]:
        count+=1
  return count