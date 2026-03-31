x = input("Enter numbers separated by space: ")
y = tuple(map(int, x.split()))
print("Tuple:", y)
print("Total elements:", len(y))
print("Last element:", y[-1])
print("Reverse tuple:", y[::-1])
if 5 in y:
    print("Yes")
else:
    print("No")
z = y[1:-1]
z = tuple(sorted(z))
print("After removing first and last and sorting:", z)
