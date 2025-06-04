# 1. Use the set() constructor to create a set of 3 favorite beverages
beverages = set(["Coffee", "Juice", "Milk"])
print("Beverages set:", beverages)

# 2. Add 2 more items to the beverages set
beverages.add("Soda")
beverages.add("Blact Tea")
print("After adding more beverages:", beverages)

# 3. Check if "microwave" is present in the set
mySet = {"oven", "kettle", "microwave", "refrigerator"}
print("Is 'microwave' in the set?", "microwave" in mySet)

# 4. Remove “kettle” from the set above
mySet.discard("kettle")  # .discard() avoids error if item doesn't exist
print("After removing 'kettle':", mySet)

# 5. Loop through the set
print("Looping through mySet:")
for item in mySet:
    print("-", item)

# 6. Add elements from a list to a set
items_set = {"pen", "book", "pencil", "mathematical set", "Rotatrim"}
items_list = ["eraser", "ruler", "sharpener"]
items_set.update(items_list)
print("Updated set after adding list elements:", items_set)

# 7. Join two sets: one with ages and one with first names
ages = {22, 27, 29, 30}
first_names = {"Karungi", "Katushabe", "Rutebuuka", "Komugisha"}
combined_set = ages.union(first_names)
print("Joined set (ages + names):", combined_set)
