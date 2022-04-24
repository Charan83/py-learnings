#   class attributes/properties/variables
#       - are defined at class level, they are shared by all objects of the class
#       - we can use them for validations (see Pet.py)


#   refer to
#       - User.py
#       - Pet.py
#       - Chicken.py


#   class methods
#       - methods with @classmethod decorator
#       - they are not concerned with instances, but the class itself
#       - can be used for validation
#       - can be use to create objects if the data is coming in different format

#   refer to
#       - User.py

#   example :
""" 
        @classmethod
        def display_active_users(cls):
        return f"There are currently {cls.active_users} active users!" 
    """
