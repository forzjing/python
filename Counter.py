def createCounter():
    res = [0]
    def counter():
        res[0] +=1
        return res[0]
    return counter

counter = createCounter()

print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())

##############################################
def createCounter():
    res = 0
    def counter():
        nonlocal res
        res +=1
        return res
    return counter

counter = createCounter()

print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())

###########################################
print("###########")
def createCounter():
    res = [0]
    print( res[0])
    print(   " this is variable in outside")
    def counter():
        print( res[0] )
        print( " this is variable in side" )
        res[0] = res[0]+1
        return res[0]
    return counter

counter = createCounter()

print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())

print("############################")

def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())