classmates = ['Michael', 'Bob', 'Tracy']
# list 可以修改
print(classmates)

print( classmates[-1])
print( classmates[0])

classmates.append("Adam")
classmates.insert(-1,"Jack")
classmates.pop(-1)

classmates[-1] = "Sarah"
print(classmates)

L = ["Apple",123,True]
s = ['python', 'java', ['asp', 'php'], 'scheme']

print(s[2][1])

#tuple不能修改
t= (1,2)
print(t)

t=(1,)
print(t)

t =("a", "b",["A","B"])
t[2][0] = "X"
t[2][1] = "Y"
print(t )

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])

if L:  #只要L是非零数值、非空字符串、非空list等，就判断为True，否则为False
    print(L)

height = input("input height:\n")
weight = input("input weight:\n")
bmi = round( int(weight)/int(height)*int(height) ,2)
if bmi<18.5:
    print("thin")
elif bmi<25:
    print ("normal")
elif bmi<28:
    print("fat")
elif bmi<32:
    print("too fat")
else:
    print("unknow")
print("bmi = %.2f %% " % bmi)
