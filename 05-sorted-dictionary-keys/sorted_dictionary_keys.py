def sorted_dictionaries_keys(fruits):
    return sorted(fruits.keys()) #sorted keys alphabetically

fruits = {
    "watermelons": 1,
    "bananas": 122,
    "apples": 123,
    "oranges": 133,
    "grapes" : 23
}

print(*fruits.keys())

print(sorted_dictionaries_keys(fruits))
