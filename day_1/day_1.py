# 30 Days of Python Day 1 -- Woohoo!
# I have a little experience with Python so the first few days here might be a little light for me, but I think it will be good to review :)

import math

# LEVEL 1+2 

# Question 1 - Using Operations
print('Level 2, Question 1')
print(54 + 46)      # addition(+)
print(1000 - 1234)  # subtraction(-)
print(25 * 5)       # multiplication(*)
print(5 % 3)        # modulus(%)
print(10 / 2)       # division(/)
print(5 ** 3)       # exponential(**)
print(6 // 4)       # floor division operator(//)

# Question 2 - Creating Strings
print('Level 2, Question 2')
print('Leif')
print('Hill')
print('Canada')
print('I am enjoying 30 days of python!')

# Question 3 - Checking Data Types
print('Level 2, Question 3')
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Leif'))
print(type('Hill'))
print(type('Canada'))

# LEVEL 3

# Question 1 - Examples of Python Data Types
print('Level 3, Question 1')
print(type(5))                                          # integer/int
print(type(1.1))                                        # float
print(type(5 + 1j))                                     # complex
print(type('Hello, World!'))                            # string/str
print(type(True))                                       # boolean/bool
print(type(['Desk', 'Monitor', 'Keyboard', 'Mouse']))   # list - notation: []
print(type(('Up', 'Down', 'Left', 'Right')))            # tuple - notation: ()
print(type({5, 8, 1, 2}))                               # set - notation: {}
print(type({                                            # dictionary/dict - notation: {} (multiline with comma separators)
            'first_name':'Leif',
            'last_name':'Hill',
            'age':18,
            'is_awesome':True,
            }))


# Question 2 - Euclidian Distance between 2 Points
print('Level 3, Question 2')

# formula: d(p,q) = sqrt((p1 - q1)^2 + (p2 - q2)^2)
# points (2,3) and (10,8)

print(math.sqrt(((2 - 10)**2)+((3 - 8)**2)))