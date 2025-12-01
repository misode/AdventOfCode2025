
with open("in.txt", "r") as f:
  input = [l.strip() for l in f.readlines()]

rot = 50
p1 = 0
p2 = 0

for line in input:
  right = line.startswith("R")
  num = int(line[1:])
  for i in range(num):
    rot += 1 if right else -1
    if rot < 0:
      rot = 99
    if rot > 99:
      rot = 0
    if rot == 0:
      p2 += 1
  if rot == 0:
    p1 += 1

print(p1)
print(p2)
