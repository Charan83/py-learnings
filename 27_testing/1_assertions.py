#   Assertions
#   - 'assert' keyword is used
#   - assert accepts an expression
#   - Returns None if the expression is truthy
#   - Raises an AssertionError if the expression is falsy
#   - Accepts an optional error message as a second argument
#   - Python file when run with -O floag, assertions will not be evaluated

def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive"
    return x + y


print(add_positive_numbers(1, 3))
print(add_positive_numbers(1, -3))
