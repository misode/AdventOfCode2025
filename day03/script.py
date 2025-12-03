
with open("in.txt", "r") as f:
  input = [l.strip() for l in f.readlines()]

def find(n: int):
  joltage = 0
  for line in input:
    digits = [int(c) for c in line]
    batteries = []
    start = 0
    for i in range(n):
      end = -(n-1-i) if i < n-1 else None
      battery = max(digits[start:end])
      start = digits.index(battery, start) + 1
      batteries.append(str(battery))
    joltage += int("".join(batteries))
  return joltage

print(find(2))
print(find(12))
