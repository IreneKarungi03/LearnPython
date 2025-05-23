# 1. Concatenate an integer and a string using the correct method
age = 25
name = "I am "
result = name + str(age)  # Convert int to string before concatenation
print("Concatenated result:", result)

# 2. Remove spaces from beginning, middle, and end of the string
txt = "      Hello,       Uganda!       "
cleaned_txt = txt.strip().replace(" ", "")
print("String without any spaces:", cleaned_txt)

# 3. Convert the value of ‘txt’ to uppercase
uppercase_txt = txt.upper()
print("Uppercase:", uppercase_txt)

# 4. Replace character ‘U’ with ‘V’
replaced_txt = txt.replace("U", "V")
print("Replaced 'U' with 'V':", replaced_txt)

# 5. Return a range of characters (2nd, 3rd, and 4th) in the string
y = "I am proudly Ugandan"
substring = y[1:4]  # Indexing starts at 0; 1 is 2nd character
print("2nd to 4th characters:", substring)

# 6. Correct a string with quotation marks
# Problem: x = “All “Data Scientists” are cool!” ← causes syntax error
# Fix: Use escape characters or different quotation types
x = 'All "Data Scientists" are cool!'  # Correct version
print(x)
