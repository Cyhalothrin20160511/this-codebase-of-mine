# Given input string with numbers separated by spaces
input_str = "5900 5752 5763 5764 5773 5774 5775 5776 5777 5789 5790 5792 5793 5803 5805 5806 5807 5808 5818 5819 5820 5821 5822 5823 5833 5834 5835 5836 5837 5838 5850 5851 5852 5865 5867 5883 5884 5885 5899 5901 5902 5903 5904 5918 5932 5946 5965 5975 5976 5984 5985 5994 5919 5886 5868    "

# Convert the string to a list of numbers
numbers = list(map(int, input_str.split()))

# Sort the numbers
sorted_numbers = sorted(numbers)

# Convert the sorted list back to a string with space-separated numbers
sorted_numbers_str = ' '.join(map(str, sorted_numbers))

# Output the sorted result
print(sorted_numbers_str)
