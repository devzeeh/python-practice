# A tuple looks a lot like a list, but with one key difference
# it's immutable — once created, you can't change it
# (no append, no remove, no editing items)

date = (2026, 9, 3)
print(date[0]) # print 2026, index 0 (0, 1, 2)
print(date[2])
date[0] = 2027 # error 'tuple' object does not support item assignment