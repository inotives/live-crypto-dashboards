## Python for Data Analysis

Python has emerged as one of the most popular programming languages for data analysis due to its simplicity and the availability of powerful libraries like pandas, numpy, and matplotlib. For anyone starting out in data analysis, understanding the core functions in Python can significantly enhance your ability to manipulate, analyze, and visualize data. This article covers essential Python functions commonly used in data analysis, from the basics to more advanced tools.

#### Python Fundamental for Data Analysis

##### 1. Data Structures

List, Sets, Dictionary and Tuple are the 4 most common data structure in python. Each with distinct characteristics and use cases. Below is a detailed explanation of each of these data structures, along with how they differ in terms of functionality, structure, and performance.

###### 1.1 Python `dict` (Dictionary)
A dict (short for dictionary) is an unordered collection of key-value pairs, where each key is unique. It allows you to store data in a structured way, enabling fast lookups, insertions, and updates based on the keys. a dict store data as key-value pairs, where key must be unique & immutable, whereas value can be any data type. 
Common operations:
```
# Creating a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'} 

# accessing a dictionary
print(my_dict['name'])  # Output: Alice
print(my_dict.get('name')) # Output: Alice
print(my_dict.get('country', 0)) # Output: 0, get() method return None if key not found. you can specify what to return if None. 

# Adding or updating a key-value pair:
my_dict['age'] = 31  # Updates the 'age' key
my_dict['country'] = 'USA'  # Adds a new key-value pair

# Deleting key value pair
del my_dict['city']  # Removes the key 'city'

# Checking if key exits: 
if 'name' in my_dict:
    print("Key exists")
```

Use Case:
Dictionaries are ideal when you need to map relationships between two pieces of data, such as looking up the price of a product by its name, or storing user information like name, email, and address in a database.

##### 1.2 Python `list`
A list is an ordered collection of elements that allows you to store multiple items in a single variable. Lists are similar to arrays in other programming languages but are more flexible as they can store elements of different data types. Lists maintain the order of elements as they are inserted. You can access elements based on their position (index). Each element in a list is associated with an index, starting from 0. Lists can have duplicate elements.
Common Operations: 
```
# Creating a list 
my_list = [10, 20, 30, 40]

# Accessing element in a list
print(my_list[1])  # Output: 20

# Adding an element to a list
my_list.append(50)  # Adds 50 to the end of the list

# Inserting elements at specific position
my_list.insert(2, 25)  # Inserts 25 at index 2

# Removing elements
my_list.remove(20)  # Removes the first occurrence of 20
my_list.pop()  # Removes the last element (40)

# Slicing a list (extracting a portion of a list)
print(my_list[1:3])  # Output: [20, 25] (elements from index 1 to 2)
```

Use Case:
Lists are commonly used for sequential data, where you need to maintain the order of elements, such as storing a list of names, a series of numbers, or items in a shopping cart.

##### 1.3 Python `Set`
A set is an unordered collection of unique elements. It is primarily used when you need to store items without duplicates and when the order of items doesn't matter. Sets automatically remove duplicates, so each element appears only once. Since sets are unordered, you cannot access elements using an index.
Common Operations: 
```
# Creating a set
my_set = {1, 2, 3, 4}

# Adding element
my_set.add(5)  # Adds 5 to the set

# Removing element
my_set.remove(3)  # Removes 3 from the set

# Checking if exist in a set
if 2 in my_set:
    print("2 is in the set")

# Set Operations: union, intersection and difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5}
print(set1.intersection(set2))  # Output: {3}
```

Use Case:
Sets are ideal for cases where you want to remove duplicates from a collection or when you need to perform fast membership checks (e.g., checking if an element exists in a set). They are also useful for mathematical operations like unions and intersections.


##### 1.4 Python `Tuple`
A tuple is an ordered, immutable collection of elements in Python. Tuples are similar to lists in that they can store multiple items, but they differ in one key aspect: tuples cannot be modified once they are created. This immutability makes them useful in scenarios where data integrity is crucial. Tuples are more memory-efficient and faster than lists, especially when you don't need to modify the data. Since they are immutable, Python can optimize their storage and performance better.
Common Operations: 
```
# Creating a tuple
my_tuple = (10, 20, 30, 40) # Or my_tuple = 10, 20, 30, 40  # You can create a tuple without parentheses as long as it's clear that you're assigning multiple elements to a single variable

# Accessing element by index
print(my_tuple[1])  # Output: 20

# Slicing a tuple
print(my_tuple[1:3])  # Output: (20, 30)

# Concatenating two tuples
tuple1 = (1, 2)
tuple2 = (3, 4)
tuple3 = tuple1 + tuple2
print(tuple3)  # Output: (1, 2, 3, 4)

# Unpacking a tuple (assigning elements to variables)
a, b, c = (1, 2, 3)
print(a, b, c)  # Output: 1 2 3

# Nested tuple
nested_tuple = (1, (2, 3), 4)
print(nested_tuple[1])  # Output: (2, 3)

```

Use Cases:
Storing fixed collections: For example, storing geographic coordinates (latitude, longitude) where the order and values must remain unchanged.
Returning multiple values from a function: Since tuples can store multiple data points, they are often used when a function returns more than one value.


##### 2. Common Python functions for Data analysis

###### 2.1 Python `zip()`
The `zip()` function in Python is used to combine two or more iterables (like lists, tuples, or sets) into a single iterator of tuples. Each tuple contains one element from each of the iterables, paired together by their position (index). It effectively "zips" the iterables together, creating a tuple for each pair (or group) of elements from the inputs.
Common usage: 

- The zip() function pairs elements from each iterable based on their index. The first element from each iterable will form the first tuple, the second element will form the second tuple, and so on. 
```
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
```
- If the input iterables are of different lengths, zip() will stop when the shortest iterable is exhausted, leaving out the extra elements from the longer iterables.
```
list1 = [1, 2, 3, 4]
list2 = ['a', 'b']

zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b')]
```
- You can also "unzip" a zipped object back into individual iterables using the * operator:
```
zipped = [(1, 'a'), (2, 'b')]
unzipped = zip(*zipped)
print(list(unzipped))  # Output: [(1, 2), ('a', 'b')]
```

Use Cases of zip() in Data Analysis
- Combining Columns of Data: In data analysis, you often have data stored in separate lists or arrays, such as one list for a column of dates and another for a column of values. zip() is useful for combining these columns into a single structure (e.g., for building a DataFrame).
```
dates = ['2024-01-01', '2024-01-02', '2024-01-03']
prices = [100, 102, 98]

data = list(zip(dates, prices))
print(data)  # Output: [('2024-01-01', 100), ('2024-01-02', 102), ('2024-01-03', 98)]
```
- Creating Dictionaries from Two Lists: zip() can be used to create a dictionary by combining one list as keys and another as values. This is particularly useful when you have structured data that needs to be converted into a key-value mapping.
```
keys = ['name', 'age', 'location']
values = ['Alice', 30, 'New York']

my_dict = dict(zip(keys, values))
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'location': 'New York'}
```

- Iterating Through Multiple Data Structures Simultaneously: In data analysis, you may need to perform operations on corresponding elements from multiple lists. zip() allows you to iterate over multiple lists (or other iterables) in parallel, simplifying this process.
```
cities = ['New York', 'Los Angeles', 'Chicago']
populations = [8419600, 3980400, 2716000]

for city, population in zip(cities, populations):
    print(f"The population of {city} is {population}.")

Output: 
The population of New York is 8419600.
The population of Los Angeles is 3980400.
The population of Chicago is 2716000.
```

- Pairing Data with Labels: If you have a list of data and a corresponding list of labels (such as column headers), zip() can help to pair these together, which can be helpful for constructing data structures or outputting data.
```
headers = ['Name', 'Age', 'City']
row = ['John Doe', 28, 'San Francisco']

data = dict(zip(headers, row))
print(data)  # Output: {'Name': 'John Doe', 'Age': 28, 'City': 'San Francisco'}
```

- Working with Pandas DataFrames: In some cases, you might have to combine multiple lists to form rows or columns in a pandas DataFrame. zip() can assist in this process by efficiently grouping data before it's inserted into the DataFrame.
```
import pandas as pd

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['New York', 'Los Angeles', 'Chicago']

df = pd.DataFrame(list(zip(names, ages, cities)), columns=['Name', 'Age', 'City'])
print(df)
```

- Reshaping Data: When reshaping or reorganizing data, such as creating new features or transforming rows into columns, zip() can be helpful to group elements and restructure datasets for analysis.
```
# Transpose rows into columns
rows = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
columns = list(zip(*rows))
print(columns)  # Output: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```

In data analysis, zip() is a versatile function that helps simplify operations where multiple lists or arrays need to be processed together, such as building datasets, creating dictionaries, or iterating over multiple data points simultaneously.