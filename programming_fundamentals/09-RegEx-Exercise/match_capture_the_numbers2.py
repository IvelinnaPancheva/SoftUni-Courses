import re

pattern = r"[0-9]+"
while True:
    text = input()
    if text:
       match = re.findall(pattern, text)
       if match:
           print(" ".join(match), end=" ")
    else:
        break

