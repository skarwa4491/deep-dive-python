letters = ['B', 'D', 'C', 'a']

sorted_letters = sorted(letters, key=lambda s: s.upper())
print(sorted_letters)

dictionary = {"def": 200, " xyz ": 50, "pqr": 100}
sorted_based_on_values = dict(sorted(dictionary.items(), key=lambda x: x[1]))
print(sorted_based_on_values)
