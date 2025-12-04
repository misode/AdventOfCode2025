
with open("in.txt", "r") as f:
  input = [l.strip() for l in f.readlines()]

G = [list(line) for line in input]
N = len(G)
assert len(G[0]) == N

def find_removable(G: list[list[str]]):
  removable = []
  for r in range(N):
    for c in range(N):
      if G[r][c] != '@':
        continue
      adj = 0
      for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
          if dr == 0 and dc == 0:
            continue
          rr, cc = r+dr, c+dc
          if rr < 0 or cc < 0 or rr >= N or cc >= N:
            continue
          if G[rr][cc] == '@':
            adj += 1
      if adj < 4:
        removable.append((r, c))
  return removable

p1 = len(find_removable(G))

p2 = 0
while True:
  removable = find_removable(G)
  if not removable:
    break
  for (r, c) in removable:
    G[r][c] = '.'
    p2 += 1

print(p1)
print(p2)
