'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''

data = {"make_float": True, "operation": "add", "first": 20,
        "second": 30, "message": "Adding 2 numbers!"}


def calculate(**kwargs):
    print(f"{kwargs}")
    operation_lookup = {
        "add": kwargs.get("first", 0) + kwargs.get("second", 0),
        "substract": kwargs.get("first", 0) - kwargs.get("second", 0),
        "multiply": kwargs.get("first", 0) * kwargs.get("second", 0),
        "divide": kwargs.get("first", 0) / kwargs.get("second", 1),
    }
    is_float = kwargs.get("make_float", False)
    operation_val = operation_lookup.get("operation")
    if is_float:
        final = f"{kwargs['message']} {'The result is : '}{float(operation_val)}"
    else:
        final = f"{kwargs['message']} {'The result is : '}{int(operation_val)}"
    print(f"final value : {final}")
    return final


calculate(make_float=False, operation='add',
          message='You just added', first=2, second=4)
