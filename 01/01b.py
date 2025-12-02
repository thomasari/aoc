
rotations = []

with open("./1.txt") as f:
    rotations = [line.strip() for line in f.readlines()]

dial = 50
secret_password = 0

for rotation in rotations:
  for i in range(int(rotation[1:])):
    if rotation[0] == "L":
      dial -= 1
    elif rotation[0] == "R":
      dial += 1
    dial = dial % 100
    if dial == 0:
      secret_password += 1

print("The secret password is:", secret_password)
