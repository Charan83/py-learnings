# task 1
from random import choice
from xxlimited import foo  # DON'T CHANGE!
user_info = {
    "Student Name": "Guru",
    "Grade": 'A',
    "Score": 911,
    35: 'address'
}
print(f"user_info : {user_info}")

user_info_using_dict = dict(student_name='Guru', grade='A', score=911)
print(f"user_info_using_dict : {user_info_using_dict}")

# task 2
artist = {
    "first": "Neil",
    "last": "Young",
}
full_name = artist["first"] + ' ' + artist["last"]
print(f"full_name : {full_name}")
full_name_using_format = "{} {}".format(artist["first"], artist["last"])
print(f"full_name_using_format : {full_name_using_format}")
full_name_using_f = f"{artist['first']} {artist['last']}"
print(f"full_name_using_f : {full_name_using_f}")

#   task 3
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5,
                 stan=150.0, lisa=50.25, harrison=10.0)
print(donations)
total_donations = 0
for donation in donations.values():
    total_donations += donation
print(f"total_donations = {total_donations}")


#   task 3 : dict methods (get), 'in'
food = choice(["cheese pizza", "quiche",
              "morning bun", "gummy bear", "tea cake"])
print(f"food : {food}")

bakery_stock = {
    "almond croissant": 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}
# DON'T CHANGE above given code for this task!
if food in bakery_stock.keys():
    print(f"{bakery_stock.get(food)} left")
else:
    print("we don't make that")
# Alternative sollution
""" 
quantity = bakery_stock.get(food)
if quantity:
    print("{} left".format(quantity))
else:
    print("we don't make that") 
"""

#   task 3 : dict methods (fromKeys)
# DO NOT TOUCH game_properties!
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo",
                   "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]
initial_game_state = dict.fromkeys(game_properties, 0)
print(f"initial_game_state : {initial_game_state}")


#   task 4 : dict methods (fromKeys)
inventory = {'croissant': 19, 'bagel': 4,
             'muffin': 8, 'cake': 1}  # DON'T CHANGE THIS LINE!
# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list = inventory.copy()
print(f"stock_list after copy : {stock_list}")
# add the value 18 to stock_list under the key "cookie"
stock_list.update({"cookie": 18})
print(f"stock_list after update with 'cookie' item : {stock_list}")
# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop("cake")
print(f"stock_list after removing 'cake' : {stock_list}")
