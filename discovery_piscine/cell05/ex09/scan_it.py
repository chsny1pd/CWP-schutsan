import re

key = input()
text = input()

found = len(re.findall(key, text))
if found:
    print(found)
else:
    print("none")