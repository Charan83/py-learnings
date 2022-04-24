#   single underscore
#       - _<name> : private variable of a class (only convension as in python everything is public)

#   __<name>__
#       - __init__() : we dont define these normally, only when we want to overwrite python special methods like __init__

#   __<name>
#       - name mangling : when we put '__' before a name, python will under the hood change the name of the attribute and change it to _<Class_name>__<name>
#       - ex : __msg => _User__msg
