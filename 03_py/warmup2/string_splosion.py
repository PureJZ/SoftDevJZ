def string_splosion(str):
  str1=""
  for i in range(len(str)+1):
    str1+=str[0:i]
  return str1
