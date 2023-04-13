import sys
import itertools

# Reading the input
tokens = sys.stdin.read().split()

# Parsing the input
stones_count = int(tokens[0])
stones_weights = [int(stone_weight) for stone_weight in tokens[1:]]

# Giving the result if we have only one stone
if stones_count == 1:
    print(stones_weights[0])
    sys.exit()

# Calculating the sum and the half of the sum
sum_weight = sum(stones_weights)
half_weight = int(sum_weight / 2)

# Looking for a combination with the sum that is nearest to the half of the sum
diff = half_weight
for i in range(1, stones_count):
    combinations = itertools.combinations(stones_weights, i)
    for combination in combinations:
        new_diff = half_weight - sum(combination)
        if 0 <= new_diff < diff:
            diff = new_diff

# Printing a result
print(sum_weight - (half_weight - diff) * 2)
