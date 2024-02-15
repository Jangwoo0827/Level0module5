"""
Create algorithms and use to solve
https://central.jointheleague.org/levels/Level0/Recipes/ForLoopGauntlet.html
"""


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
for a in range(101):
    print(a1)
    a1 = a1 + 1

for a in range(101):
    print(a2)
    a2 = a2 - 1
for a in range(50):
    print(a3)
    a3 = a3 + 2
for a in range(50):
    print(a4)
    a4 = a4 + 2
for a in range(250):
    print(a5, "is odd")
    a5 = a5 + 1
    print(a5, "is even")
    a5 = a5 + 1
for a in range(112):
    print(a6)
    a6 = a6 + 7
for a in range(13):
    print("In", a7_2, "I was", a7_1, "years old.")
    a7_2 = a7_2 + 1
    a7_1 = a7_1 + 1
