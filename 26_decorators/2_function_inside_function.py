from random import choice


def greet(person):
    def get_mood():
        msg = choice(('Hello There!', 'Go away', 'I love you'))
        return msg

    return f"{get_mood()} {person}"


print(greet('Guru'))
print(greet('charan'))
