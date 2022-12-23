
# 练习3-8 放眼世界

places=['hebei','chengde','hainan','haikou','boao']

# 原始顺序
print(places)

# 按照字母排序 顺序与逆序
print((sorted(places)))
print(sorted(places,reverse=True))

# 改变列表排列顺序 再改回来
places.reverse()
print(places)
places.reverse()
print(places)

# 该表列表改为字母顺序排序和字母逆序排序
places.sort()
print(places)
places.sort(reverse=True)
print(places)