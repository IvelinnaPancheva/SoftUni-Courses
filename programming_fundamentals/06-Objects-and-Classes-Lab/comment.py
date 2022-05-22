class Comment:
    num_of_users = 0

    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes
        Comment.num_of_users += 1


com1 = Comment("ivanivanov", "i recommend this author", 2)
com2 = Comment("rada.koleva", "this article is crap", 1)
com3 = Comment("angel.kolev", "it is true", 2)
print(com1)
print(com1.username)
print(com2.content)
print(com3.likes)
print(Comment.num_of_users)

