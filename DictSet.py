d = {"Michael":95,"Bob":75,"Tracy":85}
print(d["Michael"])

d["Bob"] =100
print(d["Bob"])

print("Thomas" in d )

print(d.get("Thomas",-1))

d.pop("Bob")
print(d)
# list不能作为key

# 和list比较，dict有以下几个特点：
#
#     查找和插入的速度极快，不会随着key的增加而变慢；
#     需要占用大量的内存，内存浪费多。
#
# 而list相反：
#
#     查找和插入的时间随着元素的增加而增加；
#     占用空间小，浪费内存很少。
#
# 所以，dict是用空间来换取时间的一种方法。

s = set([1,2,2,2,4,3,5,16,7,"sss",-1,10,100])
s.add("ee")
s.remove(-1)
#无序不重复的集合
print("set s =", s)

s1=set([1,2,3])
s2=set([3,4,5])
print("set s1|s2",s1|s2)
print("set s1&s2",s1&s2)
#list类型无法放入set，  unhashable错误
# L = [1,2,3]
# s3=set([1,2,3,L])
# print("set s3=",s3)

a="abc"
b=a.replace("a","A")
print( " a replace =", a)
print( " b replaced =", b)


# t= tuple(1,2,3)
t= (1,2,3)
s=set(t)
print(" tuple in set", s)

# L=[1,2,3]
# t1=(1,2,3,L)
# s1=set(t1)
# print(" tuple(list) in set", s1)
