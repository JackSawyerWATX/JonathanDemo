state = 'web junkie'
age = 45
name = 'Jonathan'

print('My name is', name, 'and I\'m a', state,'.')

# This method places any punctuation at the end of the print, where 
# the above method places a space between the statement and the punctuation.

# Start doing it this way!
print('My name is {} and I\'m a {}.'.format(name, state))

sentence = 'My name is {} and I\'m a {}.'.format(name, state)
print(sentence)

if age > 18:
    print('You are old enough to vote.')
else:
    print('You better get to class!!')


year = int(input("Enter a year: "))

if 2000 <= year <= 2100:
    print('The year is {}. Welcome to the 21st century!'.format(year))
else:
    print('The year is {}. You are before or after the 21st century.'.format(year))


def hello(string):
    print('Goodbye ' + string)
    print('Hello {}!'.format(string))

hello(input('Enter your name: '))

def greeting(name = 'Jonathan', age = 46):
    return 'Hello {}! You are {} years old today.'.format(name, age)

greet = greeting()

print(greet)

def tripleprint():
    print("hello")
    print("hello")
    print("hello" + "hello" + "hello")

tripleprint()

def tripleprint(string = 'hella'):
    print(string + string + string)

tripleprint()

terriers = ['Jack Russell', 'Norwich', 'Yorkshire', 'Rat']
print(terriers)
print(len(terriers))
terriers.insert(2, "Irish" )
print(terriers)
print(len(terriers))
del(terriers[4])

print(terriers)
print(len(terriers))
print(terriers[2])

print()
for dog in terriers:
    print(dog)

for x in range(1, 10):
    print(x)

i = 25

while i < 30:
    print(i)
    i += 1

president = {
    1: 'George Washington',
    2: 'John Adams',
    3: 'Thomas Jefferson',
    4: 'James Madison',
    5: 'James Monroe',
    6: 'John Quincy Adams',
    7: 'Andrew Jackson',
    8: 'Martin Van Buren',
    9: 'William Henry Harrison',
    10: 'John Tyler',
    11: 'James K. Polk',
    12: 'Zachary Taylor',
    13: 'Millard Fillmore',
    14: 'Franklin Pierce',
    15: 'James Buchanan',
    16: 'Abraham Lincoln',
    17: 'Andrew Johnson',
    18: 'Ulysses S. Grant',
    19: 'Rutherford B. Hayes',
    20: 'James Garfield',
    21: 'Chester Arthur',
    22: 'Grover Cleveland',
    23: 'Benjamin Harrison',
    24: 'Grover Cleveland',
    25: 'William McKinley',
    26: 'Theodore Roosevelt',
    27: 'William Howard Taft',
    28: 'Woodrow Wilson',
    29: 'Warren G. Harding',
    30: 'Calvin Coolidge',
    31: "Herbert Hoover",
    32: 'Franklin D. Roosevelt',
    33: 'Harry S. Truman',
    34: 'Dwight D. Eisenhower', 
    35: 'John F. Kennedy', 
    36: 'Lyndon Baines Johnson', 
    37: 'Richard Nixon',
    38: 'Gerald R. Ford',
    39: 'Jimmy Carter',
    40: "Ronald Reagan",
    41: 'George H. W. Bush',
    42: 'William J. Clinton',
    43: 'George W. Bush',
    44: 'Barack Obama',
    45: 'Donald J. Trump',
    46: 'Joseph R. Biden'}

print(president[36])
print()

def get_president_name(president_number):
    president_name = president.get(president_number)
    if president_name:
        return president_name
    else:
        return "President not found"

# Main program
while True:
    try:
        # Prompt the user for input
        user_input = int(input("Enter the number corresponding to a president (or 0 to exit): "))
        
        if user_input == 0:
            break  # Exit the program if the user enters 0
        
        president_name = get_president_name(user_input)
        print(f"President {user_input}: {president_name}")
    except ValueError:
        print("Invalid input. Please enter a number.")

print()

# words = ["Senator", "Representitive", "President"]
# definitions = ["One of two congresspersons with one vote in the Senate", "One of any number of congresspersons, based on the state's population from which they are elected, with on vote in the House of Representitive.", "One elected person, selected from a national vote, to serve as Head of State and Commander in Chief"]

dictionary = {
    "Senator": "One of two congresspersons with one vote in the Senate.",
    "Representitive": "One of any number of congresspersons, based on the state's population from which they are elected, with one vote in the House of Representitive.",
    "President": "One elected person, selected from a national vote of citizens, to serve as Head of State and Commander in Chief."}

print("President - " + (dictionary["President"]))
print("Senator - " + (dictionary["Senator"]))
print("Representitive - " + (dictionary["Representitive"]))

class Dog:
    dogInfo = 'Jack Russell'
    def bark(self, str):
        print('BARK!' + str)

mydog = Dog()
mydog.bark(' bark!')
mydog.name = 'Bumpers'
mydog.age = 7
print(mydog.name)
print(mydog.age)

print(Dog.dogInfo)

print()

class Cat:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def meow(self):
        print('Meow...')

mycat = Cat('Muffin', 5, 'Tabby')

print(mycat.name)
print(mycat.age)
print(mycat.breed)

