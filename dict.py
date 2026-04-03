# temperature = 25
# if temperature > 20:
#     print("It's a warm day!")

my_dict = {
    'name': 'Alice', 
    'age': 20, 
    'major': 'Computer Science'

}

# Accessing keys
for key in my_dict:
 print(f"Key: {key}")
print("----------------------------")
# Accessing keys and values (using keys)
for key in my_dict:
 value = my_dict[key]
 print(f"Key: {key}, Value: {value}")
print("----------------------------")
# Accessing only values
for value in my_dict.values():
 print(f"Value: {value}")
print("----------------------------")
# Accessing key-value pairs (items) - Most Pythonic way
for key, value in my_dict.items():
 print(f"Key: {key} /t Value: {value}")

