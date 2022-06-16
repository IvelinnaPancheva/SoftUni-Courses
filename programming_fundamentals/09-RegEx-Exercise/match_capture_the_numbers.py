import re

pattern = r"\d+"
while True:
    text = input()
    if text:
       match = re.findall(pattern, text)
       if match:
           print(" ".join(match), end=" ")
    else:
        break

