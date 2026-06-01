name: str = "Jhon"
age: int = "21"

"""
Examples use cases of Output in Python
"""

#using type annotation for best practice
x: str = "ABC"
y: str = "2"
z: str = "im " + str("5") + " years old"
five: int = 5

print("right after this One ->", end=" ")
print("will print on the same line.")

print(five)
print(5 + int(y)) #casting, changing type
print(x)
print(z)

print("Excuse me sir, im", 30, "years Old" )
print(f'My Name is {name}, im {age} years old')
