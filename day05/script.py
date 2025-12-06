
with open("in.txt", "r") as f:
  input = [l.strip() for l in f.readlines()]

fresh, ingredients = [p.split("\n") for p in "\n".join(input).split("\n\n")]

ranges = []
for line in fresh:
  start, end = [int(p) for p in line.split("-")]
  ranges.append((start, end))

p1 = 0
for line in ingredients:
  id = int(line)
  for start, end in ranges:
    if start <= id <= end:
      p1 += 1
      break
print(p1)

p2 = 0
last = 0
ranges.sort(key=lambda x: x[0])
for start, end in ranges:
  if last < start: # add the full range
    p2 += end-start+1
  elif end > last: # add partial range
    p2 += end-last
  last = max(last, end)
print(p2)
