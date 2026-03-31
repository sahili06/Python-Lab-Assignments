s = input("Enter source file name: ")
d = input("Enter destination file name: ")

f1 = open(s, "r")
f2 = open(d, "w")

for line in f1:
    if line.strip().startswith("#"):
        continue
    if "#" in line:
        line = line.split("#")[0] + "\n"
    f2.write(line)

f1.close()
f2.close()

print("Source File Content:")
f1 = open(s, "r")
print(f1.read())
f1.close()

print("Destination File Content:")
f2 = open(d, "r")
print(f2.read())
f2.close()
