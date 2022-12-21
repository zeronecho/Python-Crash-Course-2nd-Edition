

# 练习3-4:嘉宾名单

guests=['echo','evan','li','zhang']
print(f"嘉宾名单为：{guests[0].title()},{guests[1].title()},{guests[2].title()},{guests[3].title()}")


# 练习3-5:修改嘉宾名单

print(f"\n有一位嘉宾{guests[2].title()}无法赴约")
guests[2]='pkq'
print(f"最新嘉宾名单为：{guests[0].title()},{guests[1].title()},{guests[2].title()},{guests[3].title()}")


# 练习3-6:添加嘉宾

print("\n由于餐桌升级，额外邀请3位嘉宾")
guests.insert(0,'pikaqian1')
guests.insert(2,'pikaqian2')
guests.append('pikaqian3')
print(f"最新嘉宾名单为：{guests[0].title()},{guests[1].title()},{guests[2].title()},{guests[3].title()},{guests[4].title()},{guests[5].title()},{guests[6].title()}")

# 练习3-7:缩减名单

print("\n不出意外就要出意外了，新餐桌无法到达，现在只能邀请两位嘉宾")
print(f"很抱歉，{guests.pop(0).title()},不能邀请你")
print(f"很抱歉，{guests.pop(0).title()},不能邀请你")
print(f"很抱歉，{guests.pop(0).title()},不能邀请你")
print(f"很抱歉，{guests.pop(0).title()},不能邀请你")
print(f"很抱歉，{guests.pop(0).title()},不能邀请你")
print(f"您好，{guests[0].title()}。您好，{guests[1].title()}。邀请您俩来。")
print(guests)
del guests[0]
print(guests)
del guests[0]
print(guests)