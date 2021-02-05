"""Convert KM to meter, feet, inches and centimeter"""

km = int(input("Enter distance between two cities in KM: "))
meter = km * 1000  # 1km=1000m
feet = km * 3280.84  # since 1km=3280.84feet
inch = km * 39370.1  # since 1 km=39370.1inches
cm = km * 100000  # since 1km=100000cm

print("KM to Meter", meter)
print("KM to Feet", feet)
print("KM to Inch", inch)
print("KM to CM", cm)
