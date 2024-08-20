# Define the size of the character set and the length of the strings
character_set_size = 16  # '0987654321abcdef' has 16 characters
string_length = 16

# Calculate the total number of combinations
total_combinations = character_set_size ** string_length

# Define the speed of your processor (calculations per second)
calculations_per_second = 11258280

# Calculate the time required in seconds
time_in_seconds = total_combinations / calculations_per_second

# Convert the time to a more human-readable format (days, hours, minutes, seconds)
days = time_in_seconds // (24 * 3600)
time_in_seconds %= (24 * 3600)
hours = time_in_seconds // 3600
time_in_seconds %= 3600
minutes = time_in_seconds // 60
seconds = time_in_seconds % 60

# Print the results
print(f"Total Combinations: {total_combinations}")
print(f"Time required: {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds")