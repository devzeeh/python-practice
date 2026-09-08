# A set is an unordered collection of unique items
# no duplicates allowed, and no indexing (since there's no fixed order).

hobbies = {"code", "play", "run", "walk", "sleep"}
print(hobbies)

hobbies.add("clean")
hobbies.add("code") # adding a duplicate does nothing — already exists
print(hobbies)

hobbies.remove("sleep")
print("Print hobbies",hobbies)

nums = [1, 2, 2, 3, 3, 3, 4]
unique_nums = set(nums)
print("Print only unique",unique_nums)