x = "Camus"
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])

str1 = input("string 1: ")
str2 = input("string 2: ")
print("Yesterday I wrote a {}. I sent it to {}!".format(str1,str2))

print("aldous Huxley was born in 1894".title())

x = "Where now? Who now? When now?".split("?")
print(x)

x = ["The", "fox", "jumped", "over", "the", "fence", "."]
x = " ".join(x)
x = x[0: -2] + "."
print(x)

x = "A screaming comes across the sky"
x = x.replace("s","$")
print(x)

print("Hemingway".index("m"))

print("three " + "three " + "three ")
print("three " * 3)

x = "It was a bright cold day in April, and the clocks were striking thirteen"
comma = x.index(",")
x = x[0:comma]
print(x)
