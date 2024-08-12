import random

# Read the words from the file
with open('text.txt', 'r') as file:
    words = file.read().splitlines()

# Generate all possible pairs (combinations) of two words with a combined length > 14
combinations = [w1 + w2 for w1 in words for w2 in words if w1 != w2 and len(w1 + w2) > 14]

# Shuffle the list of combinations to randomize the order
random.shuffle(combinations)

# Select the first 100,000 combinations if there are enough, otherwise use all available
if len(combinations) > 100000:
    combinations = combinations[200000:300000]

# Write the valid combinations to "word.txt"
with open('word.txt', 'w') as file:
    file.write('\n'.join(combinations))

print(f"Random combinations with length > 14 written to 'word.txt'. Total combinations: {len(combinations)}")
