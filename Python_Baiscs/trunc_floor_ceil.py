"""Use trunc(), floor() and ceil() for numbers -2.8,-0.5, 0..2, 1.5 and 2.9
to understand the difference between these functions clearly."""

import math

val1 = -2.8
val2 = -0.5
val3 = 0.2
val4 = 1.5
val5 = 2.9

print("trunc("+str(val1)+") = ", math.trunc(val1))
print("floor("+str(val1)+") = ", math.floor(val1))
print("ceil("+str(val1)+") = ", math.ceil(val1), "\n")

print("trunc("+str(val2)+") = ", math.trunc(val2))
print("floor("+str(val2)+") = ", math.floor(val2))
print("ceil("+str(val2)+") = ", math.ceil(val2), "\n")

print("trunc("+str(val3)+") = ", math.trunc(val3))
print("floor("+str(val3)+") = ", math.floor(val3))
print("ceil("+str(val3)+") = ", math.ceil(val3), "\n")

print("trunc("+str(val4)+") = ", math.trunc(val4))
print("floor("+str(val4)+") = ", math.floor(val4))
print("ceil("+str(val4)+") = ", math.ceil(val4), "\n")

print("trunc("+str(val5)+") = ", math.trunc(val5))
print("floor("+str(val5)+") = ", math.floor(val5))
print("ceil("+str(val5)+") = ", math.ceil(val5))