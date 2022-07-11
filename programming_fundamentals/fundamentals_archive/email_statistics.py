import re
email_pattern = r"^(?P<username>[A-Za-z]{5,})@(?P<domain>[a-z]{3,}\.(bg|com|org))$"
count = int(input())
emails = {}

for x in range(count):
    email = input()
    valid_email = re.finditer(email_pattern, email)
    if valid_email:
        for match in valid_email:
            username = match.group("username")
            domain = match.group("domain")
            if domain not in emails:
                emails[domain] = [username]
            else:
                if username not in emails[domain]:
                    emails[domain].append(username)
            count = len(emails[domain])

len_is_the_same = True
for key in emails.keys():
    if len(emails[key]) != count:
        len_is_the_same = False
        break

if len_is_the_same:
    for domain, usernames in emails.items():
        print(f"{domain}:")
        for username in usernames:
            print(f"### {username}")
else:
    emails = dict(sorted(emails.items(), key= lambda x: -len(x[1])))
    for domain, usernames in emails.items():
        print(f"{domain}:")
        for username in usernames:
            print(f"### {username}")