goal=open('input.txt').read()
goal=int(goal)//10
print(goal)
check=0
num=221000
while num < goal:
    print(num,'   ',check)
    check=0
    j=1
    while j < num:
        if num%j==0:
                check+=j
                if check>=goal:
                    print(num,'   ',check)
                    goal=0
        j+=1
    num+=1
