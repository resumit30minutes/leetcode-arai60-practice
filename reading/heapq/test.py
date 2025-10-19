
import heapq

def t(lst, item):
    before = "before=" + str(lst) + ",item=" + str(item)

    heapq.heappush(lst, item)
    after = " after=" + str(lst)

    print(before + after)


t([], 4) # [4]
t([1], 2) # [1, 2]
t([2], 1) # [1, 2]
t([1,3], 2) # [1, 3, 2]