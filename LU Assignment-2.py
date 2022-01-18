#Hello
a=10;b=5
print("Integer and float")
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)
print('\n')
print('\n')

print("Boolean")
c=True; d=False
print(c and d)
print(c or d)
print(not c )
print('\n')
print('\n')


print("String")
name="Ajaf"
age=19
fld="Design"
print(name, "aged", age, "loves to do",fld)
print("Navi is friend of %s whose age is %s"%(name,age))
print(f"Hello, My name is {name} and I'm {age} years old.")
print('\n')
print('\n')


print("Tuple Integer")
tup1=(2,4,6,8,10)
print(sum(tup1))
print(min(tup1))
print(max(tup1))
print('\n')

tup2=('a','c','t')
print(min(tup2))
print(max(tup2))
print('\n')

print("Dictionary")
dict1 = {
  "brand": "MSI",
  "model": "GF75",
  "ram": 8
}
print("RAM: ",dict1["ram"])
print("Length: ",len(dict1))

