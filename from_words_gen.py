import random

# Read the words from the file
with open('text.txt', 'r') as file:
    words = file.read().splitlines()

# Generate all possible pairs (combinations) of two words with a combined length > 8
combinations = [w1 + w2 for w1 in words for w2 in words if w1 != w2 and len(w1 + w2) > 31]

# Shuffle the list of combinations to randomize the order
random.shuffle(combinations)

# Write the valid combinations to "word.txt"
with open('word.txt', 'w') as file:
    file.write('\n'.join(combinations))

print("Random combinations with length > 8 written to 'word.txt'")
