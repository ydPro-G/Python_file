number = []
for value in range(1,11):
    number.append(value**2)
print(number)


print("\nOR\n")
num = (n**2 for n in range(1,11))
print(number)
