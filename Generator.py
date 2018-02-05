L = [x*x for x in range(10)]
# print(L)

#【】变成（）就是generator
g = (x*x for x in range(10) )
# print(g)

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# for n in g:
#     print(n)
#

#斐波拉契数列
def fib(max):
    n,a,b = 0,0,1
    while n< max:
        # print(b)
        yield b
        a,b=b,a+b
        n=n+1
    return "done"

# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]
#循环获取generator
for n in fib(9):
    print (n)

print( fib(9) )

#generator生成过程
def odd():
    print("step 1")
    yield 1
    print("setp 2")
    yield (3)
    print("step 3")
    yield (5)
    return None

o=odd()
print( next(o))
print( next(o))
print( next(o))

#循环获取generator返回值
while True:
    try:
        x=next(o)
        print("g:",x)
    except StopIteration as e:
        print("generator return value", e.value)
        break



#杨辉三角形
def triangles():
    L = [1]
    while True:
        yield L
        # L = [1] + [ L[i]+L[i+1] for i in range(len(L)-1) ] + [1]
        L = [1] + [L[n] + L[n - 1] for n in range(1, len(L))] + [1]

    # 第一行：L = [1]
    # len(L) = 1
    # range(1,1) = []  # 此时， L[n-1] for n in range(1,len(L))] 这个for in 不执行
    # 第二行：L = [1] + [L[n] + L[n-1] for n in [] ] + [1]
        # L = [1] + [1]
        # L = [1, 1]
        # len(L) = 2
        # range(1,2) = [1]
    # 第三行：L = [1] + [L[n] + L[n-1] for n in [1]] + [1]
        # L = [1] + [ L[1] + L[1-1] ] + [1]
        # L = [1] + [ L[1] + L[0] ] + [1]
        # L = [1] + [ 1 + 1] + [1]
        # L = [1, 2, 1]
    #
    # 作者：审判spp
    # 链接：https: // www.jianshu.com / p / 679
    # a073d10c3
    # 來源：简书
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



# for n in triangles():
#     print (n)
times =0
n=triangles()#必须获取可遍历对象
while times<10:
    times+=1
    print( next(n )  )

print("=========")
#zip方式
def triangles():
    L = [1]
    while True:
        yield L
        L=[x+y for x,y in zip([0]+L,L+[0])]

times =0
for n in triangles():
    times += 1
    print(n)
    if times ==10:
        break


# zip([iterable, ...])
# zip()是Python的一个内建函数，它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的list（列表）。若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。利用*号操作符，可以将list unzip（解压）。
#
# 作者：审判spp
# 链接：https://www.jianshu.com/p/679a073d10c3
# 來源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

x=[0,1]
y=[1,0]
xy=zip(x,y)
print(list(xy))


print(list( zip([0]+[1],[1]+[0]) ))  #[(0, 1), (1, 0)]

print( list( x+y for x,y in zip([0,1],[1,0]) )  ) #[1, 1]
print( list( x+y for x,y in zip([0,1,1],[1,1,0]) )  ) #[1,2,1]
print( list( x+y for x,y in zip([0,1,2,1],[1,2,1,0]) )  ) #[1,3,3,1]
print( list( x+y for x,y in zip([0,1,3,3,1],[1,3,3,1,0]) )  ) #[1,4,6,4,1]