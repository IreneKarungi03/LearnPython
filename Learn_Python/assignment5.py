# Dictionary provided
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# 1. Print the value of the shoe size
print("Shoe size:", Shoes["size"])

# 2. Change the value "Nick" to "Adidas"
Shoes["brand"] = "Adidas"
print("After changing brand:", Shoes)

# 3. Add a key/value pair "type": "sneakers"
Shoes["type"] = "sneakers"
print("After adding 'type':", Shoes)

# 4. Return a list of all keys
keys = list(Shoes.keys())
print("Keys in dictionary:", keys)

# 5. Return a list of all values
values = list(Shoes.values())
print("Values in dictionary:", values)

# 6. Check if the key "size" exists
print("Does 'size' exist in dictionary?", "size" in Shoes)

# 7. Loop through the dictionary
print("Looping through dictionary:")
for key, value in Shoes.items():
    print(f"{key}: {value}")

# 8. Remove "color" from the dictionary
Shoes.pop("color", None)  # .pop() with default avoids error if key is missing
print("After removing 'color':", Shoes)

# 9. Empty the dictionary
Shoes.clear()
print("After clearing dictionary:", Shoes)

# 10. Write a dictionary and make a copy
Person = {
    "name": "Karungi",
    "age": 22,
    "city": "Kampala"
}
Person_copy = Person.copy()
print("Original dictionary:", Person)
print("Copied dictionary:", Person_copy)

# 11. Show nested dictionaries
students = {
    "student1": {
        "name": "Rutebuuka",
        "age": 29
    },
    "student2": {
        "name": "Katushabe",
        "age": 27
    }
}
print("Nested dictionaries:")
for student_id, student_info in students.items():
    print(student_id, "=>", student_info)
