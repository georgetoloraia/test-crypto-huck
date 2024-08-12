# Open the text file in read mode
with open('privs.txt', 'r') as file:
    lines = file.readlines()

# Remove duplicate lines
unique_lines = list(set(lines))

# Sort the lines if needed (optional)
unique_lines.sort()

# Open the text file in write mode to save the unique lines
with open('privs.txt', 'w') as file:
    file.writelines(unique_lines)

print("Duplicates removed.")
