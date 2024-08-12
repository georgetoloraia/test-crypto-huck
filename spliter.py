# Open the file in read mode
with open("text.txt", "r") as f:
    # Read the entire content of the file
    content = f.read()

# Split the content by commas
split_content = content.split(" ")

# Open the file in write mode to overwrite it with the new content
with open("text.txt", "w") as f:
    # Write each item from the split content on a new line
    for item in split_content:
        f.write(item.strip() + "\n")
