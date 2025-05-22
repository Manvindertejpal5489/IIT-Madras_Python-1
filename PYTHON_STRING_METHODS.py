# PYTHON STRING METHODS

#🔤 lower() Examples

print("Python".lower())                     # 1. python
print("HELLO World".lower())                # 2. hello world
print("123ABC".lower())                     # 3. 123abc
print("MiXeD CaSe".lower())                 # 4. mixed case
print("Already lower".lower())              # 5. already lower

print("----")

#🔠 upper() Examples

print("Python".upper())                     # 1. PYTHON
print("hello world".upper())                # 2. HELLO WORLD
print("123abc".upper())                     # 3. 123ABC
print("MiXeD CaSe".upper())                 # 4. MIXED CASE
print("Already UPPER".upper())              # 5. ALREADY UPPER

print("----")
# 🆙 capitalize() Examples

print("python string".capitalize())         # 1. Python string
print("HELLO world".capitalize())           # 2. Hello world
print("123abc".capitalize())                # 3. 123abc
print("mIXED Case".capitalize())            # 4. Mixed case
print(" already capitalized".capitalize())  # 5.  already capitalized
print("----")

# 📝 title() Examples

print("python string methods".title())      # 1. Python String Methods
print("HELLO world".title())                # 2. Hello World
print("123abc title".title())               # 3. 123Abc Title
print("mixed CASE example".title())         # 4. Mixed Case Example
print("title already Title".title())        # 5. Title Already Title

print("----")
# 🔄 swapcase() Examples

print("Python".swapcase())                  # 1. pYTHON
print("HELLO world".swapcase())             # 2. hello WORLD
print("123ABCdef".swapcase())               # 3. 123abcDEF
print("MiXeD CaSe".swapcase())              # 4. mIxEd cAsE
print("sWAPcASE Test".swapcase())           # 5. SwapCase tEST


print("----")

x = "Python"

print(x.startswith('P'))       # True: Starts with capital P
print(x.startswith('p'))       # False: Case-sensitive
print(x.startswith('Py'))      # True: Starts with 'Py'
print(x.startswith('yt'))      # False: Starts with 'Py', not 'yt'
print(x.startswith(('Py', 'Ty')))  # True: starts with one of the given prefixes

print("----")
x = "Python String Methods"

print(x.count('t'))      # 1. Count lowercase 't'
print(x.count('T'))      # 2. Count uppercase 'T'
print(x.count('o'))      # 3. Count letter 'o'
print(x.count(' '))      # 4. Count spaces
print(x.count('th'))     # 5. Count the substring 'th'
print("----")
x = "Python String Methods"

print(x.index('S'))      # 1. Find position of first uppercase 'S'
print(x.index('t'))      # 2. Find position of first lowercase 't'
print(x.index('o'))      # 3. Find position of first 'o'
print(x.index('n'))      # 4. Find position of first 'n'
print(x.index(' '))      # 5. Find position of first space
print("----")
x = "Python String Methods"

print(x.replace('S', 's'))        # 1. Replace uppercase 'S' with 's'
print(x.replace('M', 'm'))        # 2. Replace uppercase 'M' with 'm'
print(x.replace(' ', '_'))        # 3. Replace spaces with underscores
print(x.replace('o', '0'))        # 4. Replace 'o' with zero
print(x.replace('th', 'TH'))      # 5. Replace substring 'th' with 'TH'
