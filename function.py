# def add(a: int, b: int) -> int:
#     print(f'Adding {a} + {b}')
#     return a + b

# print(add(2, 7))

def greet(name: str, greeting: str = "Hi") -> str:
    print(f'{greeting}, {name}!')

greet('Juan')
greet('Juan', 'Good afternoon')

def hello() -> None:
    print("hello")

hello()
hello()