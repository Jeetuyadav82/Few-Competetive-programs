def subsets(nums):
  if nums is None:
      return None
  l = [[]] 
  next = [] 
  for n in nums:
    for s in l:
      next.append(s + [n])
    l += next
    next = []
  return l

p=input()# may be [int(i) for i in input().split()]
k=subsets(p)
print(k)
