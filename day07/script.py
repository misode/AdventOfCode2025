from collections import defaultdict

with open("in.txt", "r") as f:
  input = [l.strip() for l in f.readlines()]

G = [list(line) for line in input]

p1 = 0
beams = set([G[0].index("S")])
for r in range(1, len(G)):
  next = set()
  for c in beams:
    if G[r][c] == ".":
      next.add(c)
    if G[r][c] == "^":
      next.add(c-1)
      next.add(c+1)
      p1 += 1
  beams = next
print(p1)

p2 = 1
timelines = {G[0].index("S"): 1}
for r in range(1, len(G)):
  next = defaultdict(int)
  for c, count in timelines.items():
    if G[r][c] == ".":
      next[c] += count
    if G[r][c] == "^":
      next[c-1] += count
      next[c+1] += count
      p2 += count
  timelines = next
print(p2)
