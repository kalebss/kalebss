# INDEXING

# string
x = "frog"
print(x[3])

# list
x = ["pig", "cow", "horse"]
print(x[1])

# tuple
x = ("Kevin", "Niklas", "Jenny", "Craig")
print(x[0])


# SLICING
#
# [start : end+1 : step]

x = "computer"
print(x[1:4])
print(x[1:6:2])
print(x[-1])
print(x[-3:])
print(x[:-2])  ## everything except the last 2 items


###############################

# TESTING MEMBERSHIP

# string
x = "bug"
print("u" in x)

# list
y = ["pig", "cow", "horse"]
print("cow" not in y)

z = ("Kevin", "Niklas", "Jenny", "Craig")
print("Niklas" in z)


###############################

# iterating through the itesm in a sequence

# item
x = [7, 8, 3]
for item in x:
    print(item)

# index and item
y = [7, 8, 3]
for index, item in enumerate(y):
    print(index, item)


# number of items

# string
x = "bug"
print(len(x))

# list
y = ["pig", "cow", "horse"]
print(len(y))

z = ("Kevin", "Niklas", "Jenny", "Craig")
print(len(z))


# minimum / maximum

# finds the min item in a sequence lexicographically
# ,cannot mix types

x = "bug"
print(min(x))

# list
y = ["pig", "cow", "horse"]
print(min(y))

z = ("Kevin", "Niklas", "Jenny", "Craig")
print(min(z))


## sorting
# returns a new LIST of items in sorted order

x = "bug"
print(sorted(x))

# list
y = ["pig", "cow", "horse"]
print(sorted(y))

z = ("Kevin", "Niklas", "Jenny", "Craig")
print(sorted(z))


# unpacking - unpack the n items of a sequence into n variables

y = ["pig", "cow", "horse"]
a, b, c = y
print(a, b, c)


############################################

# ABOUT LISTS #

# general purpose
# most widely used
# grow and shrink size as needed
# sequence type
# sortable


# constructors - creating a new list

x = list()
y = ["a", 25, "dog", 8.42]
tuplel = (10, 20)
z = list(tuplel)
print(z)

# list comprehension
a = [m for m in range(8)]
print(a)
b = [i**2 for i in range(10) if i > 4]
print(b)


# delete - delete a list or an item
x = [5, 3, 9, 10]
del x[1]
print(x)

# append
x = [5, 3, 9, 10]
x.append(7)
print(x)


# extend
x = [5, 3, 9, 10]
y = [17, 2, 5, 240]
x.extend(y)
print(x)

# insert
x = [5, 3, 9, 10]
x.insert(1, 7)
print(x)
x.insert(1, ["a", "m"])
print(x)


# pop - pops off the last item of a list
x = [5, 3, 4]
x.pop()
print(x)
print(x.pop())

# remove - remove first instance of an item
x = [5, 3, 8, 6, 3]
x.remove(3)
print(x)


# sort vs. sorted
# x.sort - puts the items of x in sorted order (sorts in place)
# sorted(x) - returns the new sorted list without changing the original list x
x = [5, 3, 8, 6, 3]
x.sort()
print(x)

sorted(x)
print(x)


########################################

# TUPLES #

# immutable can't add/change
# useful for fixed data
# faster than lists
# sequence type


# constructors - creating new tuples
x = ()
x = (1, 2, 3)
x = 1, 2, 3
x = (2,)  # comma tells python it's a tuple
print(x, type(x))

listl = [2, 4, 6]
x = tuple(listl)
print(x, type(x))


# tuples are immuatble, but member objects may be mutable
x = (1, 2, 3)
# del(x[1]) #fails
# x[1] = 8 #fails
print(x)

y = ([1, 2], 3)  # a tuple where the first item is a list
del y[0][1]  # delete the 2
print(y)  # the list within the tuple is mutable

y += (4,)  # concatting 2 tuples works
print(y)


####################################################

# SETS

# stores non-duplicate items
# very fast acces vs. lists
# math set ops (union, intersect)
# sets are unordered

# constructors - creating new sets
x = {
    3,
    5,
    3,
    5,
}
print(x)

y = set()
print(y)

list1 = [2, 3, 4]
z = set(list1)
print(z)


# set operations
x.add
x.remove
x.clear  # delete all items
print(5 in x)  # membership
print(x.pop(), x)  # pop random item from set x


# mathematical set operations

# intersections AND
# Union OR


# dictionaries
# key/value pairs
# associative array, like java hashmap
# dicts are unordered

# sets
x = {"pork": 25.3, "beef": 33.8, "chicken": 22.7}

# lists of tuples
x = dict([("pork", 25.3), ("beef", 33.8), ("chicken", 22.7)])

# string assignment
x = dict(pork=25.3, beef=33.8, chicken=22.7)
print(x)


# dict operations
x["shrimp"] = 38.2
