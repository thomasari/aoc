id_ranges = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

with open("./2.txt", "r") as f:
  id_ranges = f.read().strip()

id_ranges = [[int(x),int(y)] for x,y in [r.split("-") for r in id_ranges.split(",")]]

invalid_id_total = 0

def validate_id(id):
  s = str(id)
  if len(s) > 1:
    for i in range(1, ((len(s)+1) // 2 + 1)):
      substrings = [s[j:j+i] for j in range(0, len(s), i)]
      if len(set(list(substrings))) == 1:
        return False
  return True

for r in id_ranges:
  for i in range(r[0], r[1]+1):
    if not validate_id(i):
      invalid_id_total += i


print(invalid_id_total)
