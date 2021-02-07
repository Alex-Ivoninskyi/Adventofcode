goal=open('input.txt').read()
goal=int(goal)//10
print(goal)
check=0
jcheck=goal
num=goal
while 1 < num:
    print(num,'   ',check)
    check=0
    j=goal
    while 1 < j:
        if num%j==0:
            check+=j
            if check>=goal:
                print(num,'yes',check)
                    
        j-=1
    num-=1
