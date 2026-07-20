def calculate(a, b):
    return a + b, a - b, a * b

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
sum_, diff, product = calculate(a,b)

print("Sum:", sum_)
print("Difference:", diff)
print("Product:", product)