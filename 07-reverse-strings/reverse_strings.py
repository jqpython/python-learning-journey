def reverse_strings(strings):
    reversed_list = [ ]
    for string in strings:
        reversed_string = string[::-1] # correct slicing to reverse the string
        reversed_list.append(reversed_string)
    return reversed_list

strings = ["der", "neerg","eulb","knip","egnaro"]
print("Colors names in Reverse Order")
print(reverse_strings(strings))
