# name = "Adrian"

# print(name)

# # string[start:end]
# print(name[1])
# # from position start to position end-1
# print(name[2:4])

# print(name[3:])

# print(name[:4])
# # counting from end to start
# print(name[-1])

# print(name[1] + name[4:])


# new_name = "X" + name[1:]

# print(new_name)

##############################################

# test = "This is a simple string to practice on"

# print(len(test))
# print(test.count('s'))
# print(test.count('is'))
# test = test.replace("string", "charactor sequence")
# print(test)
# print(test[10:16])
# print(test.find('a'))
# print(test.find('a', 10))


# print(test.split())
# print(test.split("charactor"))
# print(test.split('s'))
# print(test.split('s', 3))


# words = test.split()
# print(words)
# print(" ".join(words))
# print("...".join(words))


# print(test.upper())
# print(test.lower())
# print(test.lower().capitalize())
# print(test.title())
# print("UPPER".isupper())
# print("UpPeR".isupper())
# print("lower".islower())
# print("Lower".islower())

###########################################

print("querty123".isalnum())
print("querty'#123".isalnum())
print("letters".isalpha())
print("letters123".isalpha())
print("let ters".isalpha())
print("12345".isdigit())
print("12345abc".isdigit())
print("     ".isspace())
print("a     b".isspace())
print("A string".ljust(15))
print("A string".rjust(15))
print("A string".center(15))
print("A string".center(15).strip())
