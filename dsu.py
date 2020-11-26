"""
dsu => disjoint set union

rank is calculated based on size.
"""

class Dsu:
  def __init__(self, elements_count):
    self.parent = [x for x in range(elements_count)]
    self.rank = [1 for x in range(elements_count)]

  def find_set(self,v):
    if self.parent[v] == v:
      return v 
    self.parent[v] = self.find_set(self.parent[v])
    return self.parent[v]

  # union of two sets
  def union_sets(self, a, b):
    a = self.find_set(a)
    b = self.find_set(b)

    if a != b:
      if self.rank[a] < self.rank[b]:
        a, b = b, a
      self.parent[b] = a
      self.rank[a] += self.rank[b]

  # testing array
  # def print_arr(self):
  #   print("parent", end = " ")
  #   for x in self.parent:
  #     print(x, end=" ")
  #   print()
  #   print("rank  ", end=" ")
  #   for x in self.rank:
  #     print(x,end=" ")
  #   print()

#testing

if __name__ == "__main__":
  dsu = Dsu(10)


