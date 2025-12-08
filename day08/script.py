
initial_count = 1000
with open("in.txt", "r") as f:
  input = [l.strip() for l in f.readlines()]

P: list[tuple[int, int, int]] = []
for line in input:
  x, y, z = [int(n) for n in line.split(",")]
  P.append((x, y, z))

edges: list[tuple[int, int, float]] = []
for i, p1 in enumerate(P):
  for j, p2 in enumerate(P):
    if j <= i:
      continue
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    d = (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2
    edges.append((i, j, d))
edges.sort(key=lambda x: x[2])

parent = [i for i in range(len(P))]

def find_root(i):
  if parent[i] == i:
    return i
  return find_root(parent[i])

size = 0
for _ in range(initial_count):
  i, j, d = edges.pop(0)
  r1, r2 = find_root(i), find_root(j)
  if r1 != r2:
    parent[r2] = r1
    size += 1

circuits = {}
for i in range(len(P)):
  r = find_root(i)
  circuits[r] = circuits.get(r, 0) + 1

sizes = list(circuits.values())
sizes.sort(reverse=True)
p1 = sizes[0] * sizes[1] * sizes[2]
print(p1)

p2 = None
while edges and size < len(P)-1:
  i, j, d = edges.pop(0)
  r1, r2 = find_root(i), find_root(j)
  if r1 != r2:
    parent[r2] = r1
    size += 1
    p2 = P[i][0] * P[j][0]
print(p2)
