

# 练习2-7 剔除人名中的空白

name="     echo  "
print(name)

# 练习使用删除空白的函数
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# 练习使用符号组合
print("1 \n\t"+name.lstrip())
print("2 \n\t"+name.rstrip())
print("3 \n\t"+name.strip())