

class Car():
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 10

gangadhar = Car(user_id="002", user_name="gangadahr")
print(gangadhar.username)