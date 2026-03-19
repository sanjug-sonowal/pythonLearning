"""
Introduction to Data types
- List
- Set
- Tuples
- Dictionary

List is mutable we can change and one more thing about list is we can have multiple data types in a single list
set is mutable but elements of the set is immutable
tuple is immutable means we cannot change once it declared or stored something inside tuple
dictionary is a key value pair data structure
"""

names = ["sanjug","jarvis","thor","spiderman","hulk"]

print(names)

names.append("loki")

print(names)

names.append(30)

print(names)

subjects = {"maths","physics","chemistry"} # in set order matters means 1,2 != 2,1

print(subjects)

# subjects.append("geometry") # we cannot append in a set this is immutable

#to defin empty set
roll = set()

print(roll)


dict = {
    "name":"sanjug",
    "color":"green",
    "nation":"Indian",
    "rollno":21
}

print(dict["nation"])


