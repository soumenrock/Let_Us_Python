"""Write a program that generates 5 random numbers in the range 10 to 50. Use a seed value of 6.
Make a provision to change this seed value every time you execute the program by associating it
with time of execution."""

import random
import time

random.seed(6 + time.time())
print(random.randint(10, 50))
print(random.randint(10, 50))
print(random.randint(10, 50))
print(random.randint(10, 50))
print(random.randint(10, 50))
