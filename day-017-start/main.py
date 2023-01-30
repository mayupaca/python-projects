class User:
    # initはclassが呼ばれるたびに初期化される
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # デフォルトで設定したい場合は、初期化の引数に何も入れない
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "yuki")
# user_1.id = "001"
# user_1.username = "yuki"

user_2 = User("008", "taro")
# user_2.id = "008"
# user_2.username = "taro"

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)