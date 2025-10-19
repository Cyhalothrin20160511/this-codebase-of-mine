# Given input string with numbers separated by spaces
input_str = "24 851 895 935 977 1054 1018 936 978 979 937 896 897 938 898 854 811 855 899 729 856 812 771 725 808 767 852 809 853 810 769 453 526 605 682 490 565 642 386 454 527 606 683 418 491 566 607 643 684 726 768 727 644 567 492 419 360 337 388 456 529 608 645 685 568 493 420 361 313 338 389 457 530 609 686 646 687 647 610 570 531 494 458 390 339 315 316 293 272 292 256 257 241 226 212 227 200 153 134 116 80 98 81 36 37 16 25 10 15 8 14 7 4 3 6 13 29 20 19 11 18 26 728 770 569 528 455 387 421 362 291 273 49 65 9 17 38 27 28 12 5 1 2 22 23 53 40 41 54 51 67 242"

# Convert the string to a list of numbers
numbers = list(map(int, input_str.split()))

# Sort the numbers
sorted_numbers = sorted(numbers)

# Convert the sorted list back to a string with space-separated numbers
sorted_numbers_str = ' '.join(map(str, sorted_numbers))

# Output the sorted result
print(sorted_numbers_str)
