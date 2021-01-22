# import re
# test = "86.34.197.6:23500"
# res = re.sub(r'\:.*', "", test)
# print(res)
s = "86.34.197.6:23500"
temp = s.find(':')
index = temp
s = s[index:]
s = s[1:]
print(s)
