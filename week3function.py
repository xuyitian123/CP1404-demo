"""
function menu
"""
def get_food_item(food_list):
    food=input("Enter the food you have eaten.")
    food_list.append(food)
def check_calorie(food):
    if "fried" in food:
        return 200
    elif "steam" in food:
        return 100
    return 50
def check_range(calorie=50):#give a default value
    if calorie>500:
        return"Watch your diet"
    elif total_calorie>300:
        return"You are at borderline"
    else:
        return"You are pretty safe"
food_master_list = []
for each in range(3):
    each_food=get_food_item(food_master_list)
    total_calorie+=check_calorie(each_food)
    print(food_master_list)
    if total_calorie += check(each_food)
    print("total calorie={}".format(total_calorie))