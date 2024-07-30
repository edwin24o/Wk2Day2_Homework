# strings in Python

# strings are IMMUTABLE: once created their content cannot be changed
# You can reassing the variable name to a new string, but the original data remains unchanged 

my_string = "Hello World!"
print(id(my_string))

my_string = "Hello Python!"
print(id(my_string))

#----- indexing into a string : access individual letter in a string 

first_char = my_string[0]
print(first_char)

#----- slicing : you can grab chunk/slice of a string (substraining) using slicing 

substring = my_string[0:5]
print(substring)

#----- iterating : you can iterate over a string to access each character

for char in my_string:
  print(char)


#----- formatted strings

#---- using .format()
name = "Alice"
formatted_str = "Hello, {}".format(name)
print(formatted_str)

#---- using f-strings
formatted_str = f"Hello, {name}!"
print(formatted_str)


#---- Useful strings methods 

#--- len() : returns the numbers of characters in a string, or the length of an iterable 
test = "How many CHARACTERS are in this string"
print(len(test))

#-- .upper() : return a full uppercase version of a given string
print(test.upper())

#-- .lower() : returns a full lowercase version of a given string
print(test.lower())

#-- .isupper() : return True or False to check if all characters are uppercase or not
txt = "This is now!!"
print(txt.isupper())

#--- .title() : formats string in a title case, capitalizing every word that is seperated by a space
person = "abraham lincoln"
print(person.title())

#--- .replace(<thing to replace>, <what to replace with>) : replace a substring with a new value
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print("Using the .replace() method: ", x)

#--- .split() : splits each word seperated by a space into a list
new_txt = ''
words = txt.split()
print(words)
for word in words: #added step
  print(word)
  if word == "bananas":
    new_txt += "apples"
  else: 
    new_txt += word

print("Using a for loop: ", new_txt)

#--- .lstrip(), .rstrip(), .strip(), : allow us to strip whitespace (empty space) out of a string 
test = "                wow this class is awesome!!"
print(test)

left_strip = test.lstrip() #strip the whitespave on the left side of the string only
print(left_strip)

right_strip = test.rstrip()
print(right_strip)

reg_strip = test.strip()
print(reg_strip)

#---- "".join() : joins a list of strings together to form one single string
words = ["Let's", 'join','these', 'words', 'together!']
joined = " ".join(words)
print(joined)
another_join = "   space    ".join(words)
print(another_join)

#--- .find() : search for aword in a string and will return the index that the word starts at
txt = "Hello, welcome to my world"
found = txt.find("welcome")
print(found)

#----- .count() : counts ther occurance of a substring in the main string 
txt = "Foxy Brown is a foxy lady. Is she really a fox? Idk maybe we should ask a fox?"
print(txt.lower().count('fox')) # added the lower method to count a wider range of fox and not only be specific with the strict lettering of fox

#---- .startwith(<substring>) : returns True or False depending on whether a string start with a specified substring

people = ["Tyler", "Jeremiah", "Jeremaine", "Jasmine", "Brian", "Travis", "Dylan"]
j_team = []
for person in people:
  if person.lower().startswith('j'):
     j_team.append(person)
print(j_team)     

#--- .endswith() : returns True or False deoending on wether a strinf ends with a certain substring or not
name = "Travis"
print(name.endswith('s'))

#--- .isaplha() : returns True if the string is made Entirely of alphabetic characters
letters = 'asdfghjkl'
print(letters.isalpha())

#--- .isdigit() : returns True is a string is amde entirely of numeric characters 
nums = "1234567890"
print(nums.isdigit())

#--- .isspace() : returns True if a string is comprised entirely of only whitespaces / spaces / empty
empty_string = "  "
print(empty_string.isspace())

#--- .split() : splits your string based on apsecified substring into alist of strings, default split is on spaces

words = "This-is-one-big strings with many words"
word_list = words.split()
print(word_list)

word_list = words.split("-")
print(word_list)

flavors = input("tell me all your favorite flavors (seperated by a space please): ").split()
print(flavors)
