temp = open('input.txt').read()
for j in range(0,40):
    temp +='a'
    count = 0
    ans = ''
    for i in range(0,(len(temp) - 1)):
        if temp[i] == temp[i + 1]:
            count += 1
        else:
            count += 1
            ans += str(count) + temp[i]
            count = 0
    temp = ans
print(len(temp))
        
