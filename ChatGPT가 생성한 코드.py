# List 생성
my_list = [1, 2, 3, 4, 5]

# Tuple 생성
my_tuple = (1, 2, 3, 4, 5)

# Set 생성
my_set = {1, 2, 3, 4, 5}

# Dictionary 생성
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# 형식 출력
print("List:", type(my_list))
print("Tuple:", type(my_tuple))
print("Set:", type(my_set))
print("Dictionary:", type(my_dict))

# 형식 비교
print("\n형식 비교:")
print("List와 Tuple 비교:", type(my_list) == type(my_tuple))
print("List와 Set 비교:", type(my_list) == type(my_set))
print("List와 Dictionary 비교:", type(my_list) == type(my_dict))
print("Tuple와 Set 비교:", type(my_tuple) == type(my_set))
print("Tuple와 Dictionary 비교:", type(my_tuple) == type(my_dict))
print("Set와 Dictionary 비교:", type(my_set) == type(my_dict))
