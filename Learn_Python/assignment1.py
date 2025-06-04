# 1. Create a list with 5 names and output the 2nd item
names = ["Karungi", "Irene","Audrey", "Ainsley", "Alpha"]
print("2nd item:", names[1])  # Index 1 is the 2nd item

# 2. Change the value of the first item
names[0] = "Tyrone"
print("After changing first item:", names)

# 3. Add a sixth item to the list
names.append("Manuel")
print("After adding a sixth item:", names)

# 4. Add “Bathel” as the 3rd item
names.insert(2, "Bathel")
print("After inserting 'Bathel' as 3rd item:", names)

# 5. Remove the 4th item
del names[3]
print("After removing the 4th item:", names)

# 6. Use negative indexing to print the last item
print("Last item using negative indexing:", names[-1])

# 7. Create a new list with 7 items and print 3rd, 4th, and 5th items
colors = ["Red", "Blue", "Green", "Black", "Purple", "White", "Pink"]
print("3rd to 5th items:", colors[2:5])

# 8. Write a list of countries and make a copy of it
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda","Burundi"]
countries_copy = countries.copy()
print("Original countries:", countries)
print("Copied countries:", countries_copy)

# 9. Loop through the list of countries
print("Looping through countries:")
for country in countries:
    print("-", country)

# 10. List of animal names and sort them
animals = ["Zebra", "Elephant", "Giraffe", "Antelope", "Cheetah", "Lion", "Dog", "Cow", "Anaconda"]
animals_sorted_asc = sorted(animals)
animals_sorted_desc = sorted(animals, reverse=True)
print("Animals ascending:", animals_sorted_asc)
print("Animals descending:", animals_sorted_desc)

# 11. Output only animal names with the letter ‘a’
animals_with_a = [animal for animal in animals if 'a' in animal.lower()]
print("Animals with 'a':", animals_with_a)

# 12. Join two lists: first names and second names
first_names = ["Komugisha", "Rutebuuka", "Katushabe", "Mutoni"]
second_names = ["Sarah", "Emmanuel", "Phionah", "Princess" ]
full_names = first_names + second_names
print("Joined names:", full_names)
