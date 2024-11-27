num1 = 42 #- variable declaration
num2 = 2.3 #- variable declaration
boolean = True #- variable declaration,- Boolean
string = 'Hello World' #- variable declaration,- String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #- variable declaration,- List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #- variable declaration,- Dictionary
fruit = ('blueberry', 'strawberry', 'banana') #- variable declaration,- Tuples
print(type(fruit)) #- type check
print(pizza_toppings[1]) #- access value
pizza_toppings.append('Mushrooms') #- add value
print(person['name']) #- access value
person['name'] = 'George' #- change value
person['eye_color'] = 'blue' #- change value
print(fruit[2]) #- access value

# - conditional if else
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

#- conditional if elif else
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):  #- for loop
    print(x)
for x in range(2,5):  #- for loop
    print(x)
for x in range(2,10,3):  #- for loop
    print(x)
x = 0 #- variable declaration
while(x < 5): #- while loop
    print(x)
    x += 1 # - increment

pizza_toppings.pop() #- delete value
pizza_toppings.pop(1) #- delete value

print(person) #- access value
person.pop('eye_color') ##- delete value
print(person) #- access value

for topping in pizza_toppings:  #- for loop
    if topping == 'Pepperoni': #- conditional if
        continue                #- conditional,- continue
    print('After 1st if statement')
    if topping == 'Olives': #- conditional if
        break           #- break

def print_hello_ten_times(): #- function
    for num in range(10): #- for loop
        print('Hello')

print_hello_ten_times() #- function

def print_hello_x_times(x): #- function
    for num in range(x): #- for loop
        print('Hello')

print_hello_x_times(4) #- function

def print_hello_x_or_ten_times(x = 10): #- function
    for num in range(x): #- for loop
        print('Hello')

print_hello_x_or_ten_times() #- function
print_hello_x_or_ten_times(4) #- function


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)