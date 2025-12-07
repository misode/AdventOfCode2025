from functools import reduce

with open("in.txt", "r") as f:
  F = f.readlines()

def transpose(l):
  return list(map(list, zip(*l)))

def calculate(nums: list[str], op: str):
  nums = [int(n) for n in nums]
  if op == "*":
    return reduce(lambda x, y: x * y, nums, 1)
  elif op == "+":
    return reduce(lambda x, y: x + y, nums, 0)
  else:
    raise ValueError(op)

G = [line.split() for line in F]
H = transpose(G)
p1 = 0
for [*nums, op] in H:
  p1 += calculate(nums, op)
print(p1)

I = transpose(F)
p2 = 0
nums: list[str] = []
nums_op = None
for [*digits, op] in reversed(I):
  num = "".join(digits).strip()
  if num:
    nums.append(num)
  if op != " " and nums:
    p2 += calculate(nums, op)
    nums.clear()
print(p2)
