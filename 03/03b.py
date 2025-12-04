banks = [
  "987654321111111",
  "811111111111119",
  "234234234234278",
  "818181911112111"
]

#with open("./03.txt", "r") as f:
#  banks = f.read().strip().split("\n")

joltage = 0

for bank in banks:
  nums = [int(d) for d in bank[:12]]


  for num in range(0, len(nums)):
    for i in range(0, len(bank)-(12-num)):
      if int(bank[i]) > nums[num]:
        nums[num] = int(bank[i])

  joltage += int("".join(str(d) for d in nums))

print(joltage)

