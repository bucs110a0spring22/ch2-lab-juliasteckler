import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)


#Part B
classes_per_week = 2
cost_per_class = (cost_per_week / classes_per_week)
print("Here is the cost of a class! =", cost_per_class)
print(classes_per_week, type(classes_per_week))
print(cost_per_class, type(cost_per_class))
my_list = [18, 17, 16, 15, 14]
random_list = random.choice(my_list)
print(random_list)