#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("中文字符")

print( " ord(\"A\") 获取字符的整数形式 ", ord("A"))
print( " chr(66) 把整数表示转为字符串", chr(66))
print( " chr(25991) 把整数表示转为字符串", chr(25991))

print(r"\u4e2d\u6587 代表：","\u4e2d\u6587")

str = "ABC"
print("str = ", str)

x = str.encode("ascii")
print("str.encode('ascii') = ",x)

print(r"中文.encode('utf-8') = ", "中文".encode("utf-8"))

print(r"b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8',errors='ignore') = ",b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8',errors='ignore'))

print("len(\"ABC\") 字符数= ", len("ABC"))
print(r"len('中文') 字符数= ", len("中文"))
print(r"len('b'ABC'') 字节数= ", len(b"ABC"))
print(r"len(b'\xe4\xb8\xad\xe6\x96\x87') 字节数= ", len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(r"len('中文'.encode('utf-8')) 字节数= ", len('中文'.encode('utf-8')))

print("Integer = %d " % 12)
print("Float = %f %f %f %f" % (1.2e-5,12.3e8,1.23e9,1.23))
print("String = %s " % "ABC")
print("Hex = %x %x " % (0xa5b4c3d2,0xff00) )
print("3,1 format print %%5d ,%%05d = %5d ,%05d" % (3112,1))
print("3.141111111 format print %%.2f = %.2f" % 3.141111111)

print("Lucy 12.111 format print {0},level up {1:.2f}%".format("Lucy",12.1111))


s1=100
s2=10
print(int(s1)/int(s2))
print("%s / %s = %.3f %% " % ( s1,s2, float( int(s1)/int(s2) ) ) )