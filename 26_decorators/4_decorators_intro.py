#   Decorator
#       - are functions
#       - that wrap pther functions and enhance their behavior
#       - examples : higher order functions
#       - decorators have their own syntax, using '@' (syntactic sugar)

#   Example 1
def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great Day!")

    return wrapper


@be_polite
def greetings():
    print("My name is Guru")


greetings()
print("############")
greet = be_polite(greetings)
greet()
greet()
greet()


#   Example 2 : using syntactic sugar
def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")

    return wrapper


@be_polite  # no need to set greet = be_polite(greet)
def greet():
    print("My name is Matt.")


greet()
