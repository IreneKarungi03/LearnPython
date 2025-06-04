# 1. Output your favorite phone brand from a tuple
x = ("samsung", "iphone", "tecno", "redmi")
print("My favorite phone brand is:", x[0])  # You can change the index to your favorite

# 2. Use negative indexing to print the 2nd last item
print("2nd last item:", x[-2])

# 3. Tuples are immutable; to update "iphone" to "itel", convert to a list then back to a tuple
x_list = list(x)
x_list[1] = "itel"
x = tuple(x_list)
print("After updating 'iphone' to 'itel':", x)

# 4. Add "Huawei" to your tuple (requires converting to list and back)
x = x + ("Huawei",)
print("After adding 'Huawei':", x)

# 5. Loop through the tuple
print("Looping through tuple:")
for phone in x:
    print("-", phone)

# 6. Remove/delete the first item (convert to list first)
x_list = list(x)
del x_list[0]
x = tuple(x_list)
print("After removing first item:", x)

# 7. Using the tuple() constructor to create a tuple of Ugandan cities
cities = tuple(["Kampala", "Mbarara", "Mbale", "Arua", "Gulu"])
print("Cities tuple:", cities)

# 8. Unpack your tuple
city1, city2, city3, city4, city5 = cities
print("Unpacked cities:")
print(city1, city2, city3, city4, city5)

# 9. Print 2nd, 3rd, and 4th cities using range of indexes
print("2nd to 4th cities:", cities[1:4])

# 10. Join two tuples (first names and second names)
first_names = ("Rutebuuka", "Mwebaze", "Anyeki")
second_names = ("Charles", "Fredrick", "Walter")
full_names = first_names + second_names
print("Joined name tuples:", full_names)

# 11. Create a tuple of colors and multiply it by 3
colors = ("Red", "Black", "Green", "White")
colors_multiplied = colors * 3
print("Colors multiplied by 3:", colors_multiplied)

# 12. Return number of times 8 appears in this tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)
print("Number of times 8 appears:", count_8)
