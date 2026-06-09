exp = -1
total=0
maxexp=0
minexp=None

while exp !=0:
    exp=int(input(" What is the expense? (type 0 to stop)"))

    if exp ==0:
        break
    total+=exp

    if exp>maxexp:
        maxexp=exp
    if minexp is None or exp<minexp:
        minexp=exp

print(f"Your total expense is {total}")
print(f"Maximum expensen is {maxexp}")
print(f"minimum expense is {minexp}")
    