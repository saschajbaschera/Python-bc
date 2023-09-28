class User:
    def __init__(self, userID, username):
        self.id = userID
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1




user1 = User("20202", "Sascha")
user2 = User("23422", "Mela")

user1.follow(user2)


print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)