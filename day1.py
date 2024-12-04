import sys

with open(sys.argv[1], "r") as file:
    lines = file.readlines()

left_numbers = []
right_numbers = []

for line in lines:
    left, right = map(int, line.strip().split())
    left_numbers.append(left)
    right_numbers.append(right)

left_numbers.sort()
right_numbers.sort()

total_difference = sum(abs(left - right) for left, right in zip(left_numbers, right_numbers))

print("Total Difference Sum:", total_difference)

total_product_sum = 0

for left in left_numbers:
    count = right_numbers.count(left) 
    total_product_sum += left * count

print("Total Product Sum:", total_product_sum)
