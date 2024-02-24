"""
Create algorithms and use to solve
https://central.jointheleague.org/levels/Level0/Recipes/ForLoopGauntlet.html
"""

# "print("")" Use this after all the loop


if __name__ == '__main__':
    pass
a1 = 0
a2 = 100
a3 = 2
a4 = 1
a5 = 1
a6 = 0
a7_1 = 0
a7_2 = 2012
b1_1 = 0
b1_2 = 0
b2_1 = 1
b2_2 = 2
b2_3 = 3
b3 = 1
b4_1 = 1
bonus = 0

print("Single loops")
for a in range(101):
    print(a1)
    a1 = a1 + 1
print("")
for a in range(101):
    print(a2)
    a2 = a2 - 1
print("")
for a in range(50):
    print(a3)
    a3 = a3 + 2
print("")
for a in range(50):
    print(a4)
    a4 = a4 + 2
print("")
for a in range(250):
    print(a5, "is odd")
    a5 = a5 + 1
    print(a5, "is even")
    a5 = a5 + 1
print("")
for a in range(112):
    print(a6)
    a6 = a6 + 7
print("")
for a in range(13):
    print("In", a7_2, "I was", a7_1, "years old.")
    a7_2 = a7_2 + 1
    a7_1 = a7_1 + 1
print("")

print("Nested loops")
for b in range(3):
    b1_2 = 0
    for b1 in range(3):
        print(b1_1, b1_2)
        b1_2 = b1_2 + 1
    b1_1 = b1_1 + 1
print("")
for b in range(3):
    print(b2_1, b2_2, b2_3)
    b2_1 = b2_1 + 1
    b2_2 = b2_2 + 1
    b2_3 = b2_3 + 1
print("")
for b in range(5):
    if b3 == 1:
        print(b3, "", b3+1, "", b3+2, "", b3+3, "", b3+4, "", b3+5, "", b3+6, "", b3+7, "", b3+8, "", b3+9)
    b3 = b3 + 10
    if b3 > 1:
        print(b3, b3+1, b3+2, b3+3, b3+4, b3+5, b3+6, b3+7, b3+8, b3+9)
    b3 = b3 + 10
print("")
for b in range(6):
    for b4_3 in range(b4_1-1):
        print("*", end=" ")
    print("*")
    b4_1 = b4_1 + 1
print("")

print("**Bonus**")
for b in range(100):
    print(bonus + 100)
    bonus = bonus - 1
