
with open("in.txt", "r") as f:
  input = [l.strip() for l in f.readlines()]

p1 = 0
p2 = 0

for r in input[0].split(","):
  start, end = [int(p) for p in r.split("-")]
  for num in range(start, end+1):
    s = str(num)
    if s[:len(s)//2] == s[len(s)//2:]:
      p1 += num
    if s in (s + s)[1:-1]: # https://stackoverflow.com/a/55840779
      p2 += num

print(p1)
print(p2)
