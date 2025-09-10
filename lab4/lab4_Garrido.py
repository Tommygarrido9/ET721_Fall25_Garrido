"""
Tommy Garrido
lab 4, dictionary and functions
Sep 10, 2025
"""
print("------- Example 1: dictionary -------")
#contact dictionary with three users
contacts = {
    "Bill": "718-111-2222",
    "Martha": "646-000-3333",
    "Peter": "212-000-1111"
}
print(contacts)

# save the value of a specific key
user1 = contacts["Martha"]
print(f"user's phone number = {user1}")

# add content to the dictionary
contacts["Anna"] = "646-222-3333"
print(contacts)

#update value of a specific key
contacts["Peter"] = "800-000-0000"

print("------- Example 2: loop through a dictionary -------")
# print each key in the dictionary
for i in contacts:
    print(i)

# print each value in the dictionary
for i in contacts:
    print(contacts[i])

# print each key:value in the dictionary
for i in contacts:
    print(f"{i}: {contacts[i]}")

print("------- Example 3: length of a dictionary -------")
print(f"Dictionary has{len(contacts)} users")

print("------- Example 4: Copy a dictionary -------")
copy_contact1 = contacts.copy()
copy_contact2 = dict(contacts)
print(copy_contact1)
print(copy_contact2)

print("------- Example 5: remove a key:value pair in a dictionary -------")
print(contacts)
contacts.pop("Peter")
print(contacts)

print("------- Example 6: add a new key:value pair in a dictionary -------")
print(contacts)
contacts.update({"Lucas": "212-111-1111"})
print(contacts)

print("------- Example 7: return items, keys, and values in a dictionary -------")
print(f"Return items: {contacts.items()}")
print(f"Return keys: {contacts.keys()}")
print(f"Return values: {contacts.values()}")

print("------- Example 8: Dictionary Application -------")
# store in a dictionary the count of occurences of the words in a phrase
phrase = "to be or not to be"
list_phrase = phrase.split()
word_count_dict = {}
for word in list_phrase:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1
#print result
for word in word_count_dict:
    print(f"{word} appears {word_count_dict[word]} times")

print("------- EXERCISE -------")
users = ["peterpan@yahoo.com", "annie@hotmail.com", "Carl@hotmail.com", "martha@gmail.com", "cassie@yahoo.com","Josue@hotmail.com","John@hotmail.com"]
email_count = {}
for email in users:
    domain_email = email.split("@")[1]
    if domain_email in email_count:
        email_count[domain_email] += 1
    else:
        email_count[domain_email] = 1

for domain, count in email_count.items():
    print(f"{domain} appears {count} times")