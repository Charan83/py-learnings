class User:
    active_user_count = 0

    @classmethod
    def display_active_users(cls):
        print(f"There are currently {cls.active_user_count} active users!")

    @classmethod
    def from_string(cls, users_str):
        first, last, age = users_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age) -> None:
        self._first = first
        self._last = last
        self._age = age
        User.active_user_count += 1

    @property
    def first(self):
        return self._first

    @property
    def last(self):
        return self._last

    @property
    def age(self):
        return self._age

    def login(self):
        User.active_user_count += 1
        print(f"User Logged in!")

    def logout(self):
        User.active_user_count -= 1
        print(f"User Logged out!")

    def full_name(self):
        return f"{self.first} {self.last}"


class Moderator(User):
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self._community = community

    @property
    def community(self):
        return self._community

    def remove_post(self):
        print(f"{self.full_name()} removed post from {self.community}")


jaz = Moderator('jasmine', 'Conner', 61, 'Piano')
jaz.full_name()
print(jaz.community)
jaz.remove_post()
User.display_active_users()
