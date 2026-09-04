# Automatic Type Promotion

a = 10          # int
b = 5.5         # float
c = 2 + 3j      # complex

# # int + float = float
# result1 = a + b

# # float + complex = complex
# result2 = b + c

# # int + complex = complex
# result3 = a + c

# print("a + b =", result1, "Type:", type(result1))
# print("b + c =", result2, "Type:", type(result2))
# print("a + c =", result3, "Type:", type(result3))

print(f"the addition of a and b is {a+b} and the data type is {type(a+b)}")
print(f"the addition of b and c is {b+c} and the data type is {type (b+c)}")
print(f"the addition of c and a is {c+a} and the data type is {type (c+a)}")
