banks = [
  "987654321111111",
  "811111111111119",
  "234234234234278",
  "818181911112111"
]

with open("./03.txt", "r") as f:
  banks = f.read().strip().split("\n")

joltage = 0

for bank in banks:
  first = 0
  second = 0
  for i in range(0, len(bank)-1):
    for j in range(i+1, len(bank)):
      if int(bank[i]) > first:
        first = int(bank[i])
        second = int(bank[j])
      if int(bank[j]) > second:
        second = int(bank[j])

  joltage += int(str(first) + str(second))

print(joltage)
