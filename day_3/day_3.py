# 30 Days of Python Day 3
import math

age = 18
height = 1.75
complex_num = 1 + 1j

base = int(input('Enter base: '))
height = int(input('Enter height: '))
print('The area of the triangle is ', int(0.5 * base * height))

side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))
print('The perimeter of the triangle is ', int(side_a + side_b + side_c))

length = int(input('Enter length: '))
width = int(input('Enter width: '))
print('The area of the rectangle is ', int(length * width))
print('The perimeter of the rectangle is ', int(2 * (length + width)))

radius = int(input('Enter radius: '))
print('The area of the circle is ', 3.14 * (radius ** 2))
print('The circumference of the circle is', 2 * 3.14 * radius)

slope = 2
x_int = 2/2
y_int = 2*0 - 2

slope_2 = (10-2)/(6-2)
print(slope_2)
euclidean_distance = math.sqrt(((2 - 6)**2)+((2 - 10)**2))

if slope > slope_2:
    print('Slope 1 is {diff} units greater than slope 2.').format(diff = slope - slope_2)
elif slope < slope_2:
    print('Slope 2 is {diff} units greater than slope 1.').format(diff = slope_2 - slope)
elif slope == slope_2:
    print('Slope 1 is the same as slope 2.')

x = -3
y = (x ** 2) + (6 * x) + 9
print(y)

print(len('python') != len('dragon'))

print('on' in 'python' and 'on' in 'dragon')

print('jargon' in 'I hope this course is not full of jargon.')

print('on' not in 'python' or 'on' not in 'dragon')

print(str(float(len('python'))))

num = int(input('Enter a number: '))
print('{} is even: '.format(num), (num % 2) == 0)

print((7 // 3) == int(2.7))

print(type('10') == type(10))

print(int(float('9.8')) == 10)

hours = float(input('Enter weekly hours: '))
rate = float(input('Enter hourly wage: $'))
print('Your weekly earning is $',hours * rate)

years = int(input('Enter number of years you have lived: '))
print('You have lived for {} seconds.'.format(years * 31556952))


# I recognize here there is probably some other, less literal, way to do this. Though, following along with the material taught so far, this would technically be the only way to do this without learning more.
print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')