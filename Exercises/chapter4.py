print("Challenge 1:")
x=input("number to be squared: ")
x=int(x)
print(x**2)

print("Challenge 2:")
def f(x):
    """
    prints x
    :param x: input
    """
    print(x)
f(x)

print("Challenge 3:")
def g(x,y,z,a=2,b=3):
    return x+y+z+a+b
print(g(1,1,1))

print("Challenge 4:")
def fun1(x):
    return x/2
def fun2(x):
    return x*4
x=fun1(3)
print(fun2(x))

print("Challenge 5:")
def h(x):
    return float(x)
try:
    h("string")
except ValueError:
    print("must be a number")
