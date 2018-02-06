names = ["Michael","Bob","Tracy"]
for name in names:
    print("element name= ",name)

sum =0
for x in [1,2,3,4,5,6,7]:
    sum += x
print("[1,2,3,4,5,6,7] sum = ", sum)

sum = 0
for x in range(101):
    sum += x
print("range(101) sum = ", sum)

sum =0
n=99
while n>0:
    sum=sum+n
    n=n-2
print("0-99 odd sum=",sum)

sum =0
n=100
while n>0:
    sum=sum+n
    n=n-2

print("0-100 even sum =", sum)

n=1
while n<=100:
    if n>10:
        print("break loop now n is",n)
        break
    print(n)
    n=n+1
print("END")

n=0
while n<10:
    n=n+1
    if n%2 == 0:
        continue
    print(n)
