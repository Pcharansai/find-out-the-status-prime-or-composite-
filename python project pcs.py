l=int(input())
h=int(input())
pc=0
cc=0
for i in range(l,h+1):
    for j in range(2,i):
        if i%j==0:
            print(i,"is a composite number")
            cc+=1
            break
        else:
            print(i,"is a prime number")
            pc+=1
print(pc,"prime count")
print(cc,"composite count")
            
