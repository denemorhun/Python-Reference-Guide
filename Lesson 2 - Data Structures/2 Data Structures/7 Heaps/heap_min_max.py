# heap_min_max.py
import heapq

class MinHeap(object):
  def __init__(self): self.h = []
  def heappush(self, x): heapq.heappush(self.h, x)
  def heappop(self): return heapq.heappop(self.h)
  def __getitem__(self, i): return self.h[i]
  def __len__(self): return len(self.h)
  # return smallest item and replace with x
  def heapreplace(self, x): heapq.heapreplace(self.h, x)

class MaxHeap(MinHeap):
  def heappush(self, x): heapq.heappush(self.h, MaxHeap(x))
  def heappop(self): return heapq.heappop(self.h).val
  def __getitem__(self, i): return self.h[i].val


minh = MinHeap()
maxh = MaxHeap()
# add some values
minh.heappush(12)
maxh.heappush(12)
minh.heappush(4)
maxh.heappush(4)
# fetch "top" values
print(minh[0], maxh[0])  # "4 12"
# fetch and remove "top" values
print(minh.heappop(), maxh.heappop())  # "4 12"