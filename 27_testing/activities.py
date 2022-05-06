def eat(food, is_healthy):
    ending = "because YOLO"
    if is_healthy:
        ending = "because my body is a temple"
    return f"I'm eating {food}, {ending}"


def nap(num_hours):
    msg = f"You sleft for {num_hours} hours. long naps are NOT refreshing"
    if num_hours < 3:
        msg = f"You sleft for {num_hours} hours. Short naps are refreshing"
    return msg
