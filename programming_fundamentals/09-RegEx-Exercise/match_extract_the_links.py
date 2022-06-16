import re

pattern = r"(www.([a-zA-Z0-9]+[A-Za-z0-9\-]*)(\.[a-z]+)([\.\-a-z0-9-]*))"

valid_links = []
while True:
    text = input()
    if text:
        matches = re.findall(pattern, text)
        if matches:
            valid_links.append(matches[0][0])
    else:
        break

for link in valid_links:
    print(link)