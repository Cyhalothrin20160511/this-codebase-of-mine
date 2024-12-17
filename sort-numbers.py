# Given input string with numbers separated by spaces
input_str = "272 273 256 257 292 315 337 293 316 339 313 338 361 362 390 291 387 388 389 360 "

# Convert the string to a list of numbers
numbers = list(map(int, input_str.split()))

# Sort the numbers
sorted_numbers = sorted(numbers)

# Convert the sorted list back to a string with space-separated numbers
sorted_numbers_str = ' '.join(map(str, sorted_numbers))

# Output the sorted result
print(sorted_numbers_str)
