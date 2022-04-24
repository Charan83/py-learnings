#   try_except
#       - syntax
#           try:
#               foo
#           except NameError as err:
#               print(err)

def get(d, key):
    try:
        return d[key]
    except:
        return None


d = {"fname": "Guru", "score": 200}
print(get(d, "fname"))
print(get(d, "score"))
print(get(d, "scor"))

#   try_except_else_finally
#       - syntax
#           try:
#               foo
#           except NameError as err:
#               print(err) # runs when there is an error in try block
#           else:
#               # runs when the try block runs successfully
#           finally:
#               # runs all the time

while True:
    try:
        num = int(input("please enter a number: "))
    except:
        print("except block executed, Not a valid number!")
    else:
        print("Try block executed successfully!")
        break
    finally:
        print("This block will execute all the time!!")

print("After the try_except_else_finally blocks!!")


#   example 1
def divide(a, b):
    try:
        result = a/b
    except (ZeroDivisionError, TypeError) as err:
        print("something went wrong")
        print(err)
    else:
        print(f"{a} divide by {b} = {result}")


divide(1, 2)
divide(1, 0)
divide(1, 'a')

#   example 2
# Write a function called divide, which accepts two parameters (you can call them num1 and num2). The function should return the result of num1 divided by num2. If you do not pass the correct type of arguments to the function, it should return the string "Please provide two integers or floats". If you pass as the second argument a 0, Python will raise a ZeroDivisionError, so if this function is invoked with a 0 as the value of num2, return the string "Please do not divide by zero"

# Examples

# divide(4,2)  2
# divide([],"1")  "Please provide two integers or floats"
# divide(1,0)  "Please do not divide by zero"


def divide_ex(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Please do not divide by zero"
    except TypeError:
        return "Please provide two integers or floats"
    else:
        return result


print(divide_ex(4, 2))
print(divide_ex([], "1"))
print(divide_ex(1, 0))
