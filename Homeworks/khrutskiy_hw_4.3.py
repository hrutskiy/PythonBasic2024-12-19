import random
x = random.randint(3, 10)
random_list = [random.randint(1, 10) for _ in range(x)]
new_list = [random_list[0], random_list[2], random_list[-2]]
print(random_list, "==", new_list)