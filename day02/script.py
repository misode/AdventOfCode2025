
with open("in.txt", "r") as f:
  input = [l.strip() for l in f.readlines()]

p1 = 0
p2 = 0

for r in input[0].split(","):
  start, end = [int(p) for p in r.split("-")]
  for num in range(start, end+1):
    s = str(num)
    L = len(s)
    for n in range(2, L+1):
      if L % n != 0:
        continue
      parts = [s[i:i + L // n] for i in range(0, L, L // n)]
      if len(set(parts)) == 1:
        if n == 2:
          p1 += num
        p2 += num
        break

print(p1)
print(p2)
