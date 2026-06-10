exp=[]

stopped = False

while not stopped:
    e= int(input("What is the expense? (type 0 to stop)"))

    if e!=0:
        exp.append(e)

    else:
        stopped=True

print(f"Your expense list {exp}")
print(f"Total Expenses {sum(exp)}")
print(f"Max Expense {max(exp)}")
print(f"Min Expenses {min(exp)}")
print(f"Average Expense {sum(exp)/len(exp)}")