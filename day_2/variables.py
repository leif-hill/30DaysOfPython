# 30 Days of Python Day 2

import math

# lEVEL 1

first_name = 'Lei'
last_name = 'Hill'
full_name = 'Leif Hill'
country = 'Canada'
city = 'Leif City'
age = 18
year = 2024
is_married = False
is_light_on = True

item_one, item_two, item_three = 1,2,3

# LEVEL 2

# 1
type(first_name)
type(last_name)
type(full_name)
type(country)
type(city)
type(age)
type(year)
type(is_married)
type(is_light_on)
type(item_one)
type(item_two)
type(item_three)

# 2
len(first_name)

# 3
if len(first_name) > len(last_name):
    print('First name is {difference} character(s) longer than last name.'.format(difference = len(first_name) - len(last_name)))
elif len(last_name) > len(first_name):
    print('Last name is {difference} character(s) longer than first name.'.format(difference = len(last_name) - len(first_name)))
elif len(first_name) == len(last_name):
    print("Both names are the same length.")

# 4
num_one = 5
num_two = 4
diff = num_one - num_two
product = num_one * num_two
divison = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_divison = num_one // num_two

# 5
radius = 30
pi = math.pi
area_of_circle = pi * (radius ** 2)
circum_of_circle = 2 * pi * radius
print(area_of_circle)
print(circum_of_circle)

radius_2 = int(input('Enter the radius of the circle in meters: '))
area_of_circle_2 = pi * (radius_2 ** 2)
print('The area of the circle is {area} meters squared.'.format(area = area_of_circle_2))


# 6
first_name_input, last_name_input, country_input, age_input = input('What is your first name? '), input('What is your last name? '), input('What country are you from? '), input('How old are you? ')
print(first_name_input, last_name_input, country_input, age_input)

# 7
help('keywords')