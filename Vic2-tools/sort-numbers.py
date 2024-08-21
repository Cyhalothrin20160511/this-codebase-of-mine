# 给定的带空格的数字串
input_str = "272 273 256 257 292 315 337 293 316 339 313 338 361 362 390 291 387 388 389 360 "

# 将字符串转换为数字列表
numbers = list(map(int, input_str.split()))

# 对数字进行排序
sorted_numbers = sorted(numbers)

# 将排序后的列表转换为以空格分隔的字符串
sorted_numbers_str = ' '.join(map(str, sorted_numbers))

# 输出排序后的结果
print(sorted_numbers_str)
