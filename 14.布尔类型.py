x=True
print(x)
print(type(x)) # 输出：<class 'bool'>
print(True+10) # 输出：11，True表示1
print(False+10) # 输出：10，False表示0
print('----------------------')

# 所有对象都有一个布尔值，可使用内置函数bool()进行测试
print(bool(18)) # Ture
print(bool(0),bool(0.0)) # False False
# 总结：非零数值的布尔值都为True

# 测试字符串的布尔值
print(bool('北京')) # True
print('----------------------')

print(bool('')) # 空字符串布尔值为False
print(bool(False)) # False的布尔值为False
print(bool(None)) # None的布尔值为False
print(bool(None)) # None的布尔值为False



