print("Part 1: Lists and Dictionaries\n")

odd_numbers = list(range(23, 57, 2))[::-1]
print("a. Odd Numbers (Descending Order):", odd_numbers)

course_codes = ["ENT3003", "EEL3834", "PHY2049", "MAP2302"]
print("b. Course Codes:", course_codes)

movie_title = list("kung fu panda")
movie_title.sort()
print("c. Alphabetized Movie Title:", movie_title)


personal_info = {"name": "Jackson Turnbull", "major": "Electrical Engineering", "graduation_year": 2026}
personal_info["favorite_color"] = "Blue"
print("d. Personal Information:", personal_info)

# e.
uf_quarterbacks = {"Richardson": 2549, "Trask": 4122, "Jones": 3458, "Driskel": 3247, "Tebow": 9285}
print("e. UF Quarterbacks:", uf_quarterbacks)


print("\nPart 2: Math\n")

import math

# a.
Ra = ((25 - 19 + 6)/math.sqrt(23)) * 4**3
print("a. Result:", Ra)

# b.
Rb = 70 * math.sin(math.log(2) * math.exp(math.pi/2))
print("b. Result:", Rb)

# c.

volume_prism = 6 * 8 * 4
volume_hole = (4 / 3) * math.pi * 1**3
final_volume = volume_prism - volume_hole
print("c. Volume of Rectangular Prism with Spherical Hole:", final_volume)

# d. Distance between two points in 3D space.
p1 = (-3, 6, 2)
p2 = (1, 4, -5)
distance = round(math.sqrt(sum((p2 - p1)**2 for p1, p2 in zip(p1, p2))))
print("d. Distance between points:", distance)


print("\nPart 3: Functions\n")


def PL(voltage, current):

    power = voltage * current

    limit = power > 1000

    # Print the result
    print(f"The calculated power is {power} watts.")
    if limit:
        print("Power exceeds the 1kW limit.")
    else:
        print("Power is within the limit.")

    with open("power_results.txt", "w") as file:
        file.write(f"Calculated Power: {power} watts\nPower Exceeds Limit: {limit}")

voltage = float(input("Enter Voltage: "))
current = float(input("Enter Current: "))

PL(voltage,current)