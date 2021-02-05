"""Write a program that swaps the values of a and b.
You are not allowed to use third variable. You are not allowed to perform arithmetic on a and b."""

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))

print("Before swapping: ")
print("Value of a : ", a)
print("Value of b : ", b)

# code logic
a, b = b, a

print("After swapping: ")
print("Value of a : ", a)
print("Value of b : ", b)
