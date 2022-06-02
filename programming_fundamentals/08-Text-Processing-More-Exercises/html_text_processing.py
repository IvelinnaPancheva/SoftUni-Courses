title = input()
content = input()
comment = input()
comments = []
while comment != "end of comments":
    comments.append(comment)
    comment = input()

print(f"<h1>\n\t{title}\n</h1>")
print(f"<article>\n\t{content}\n</article>")
for comment in comments:
    print(f"<div>\n\t{comment}\n</div>")


