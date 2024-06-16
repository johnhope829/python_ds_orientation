
# number 1
import numpy as np
import math

numbers = np.array(range(1000))
multiples = ([num for num in numbers if num % 3 == 0 or num % 5 == 0])
print('question 1: ' + str(sum(multiples)))

# number 2
x = 0
y = 1
z = 0
fibonacci = [0]

while x < 4000000:
    y = y + fibonacci[z-1]
    fibonacci.append(y)
    z = z + 1
    x = max(fibonacci)

even_fibonacci = [num for num in fibonacci  if num % 2 == 0 and num < 4000000]
print('question 2: ' + str(sum(even_fibonacci)))

# number 3

num = 600851475143 
x = 2

while x < math.sqrt(num):
    while num % x == 0:
        num = num / x
    x = x + 1

num = int(num)

print('question 3: ' + str(num) )