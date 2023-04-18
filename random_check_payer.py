import random

# a way to input names
names_string = input("Give me everybody's names, separated by a comma. ")

# split into list
names = names_string.split(", ")

# get the total number of items in the list
num_items = len(names)

random_choice = random.randint(0, num_items - 1)

# print(random_choice)

person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal")


# using random.choice
person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal")