# The messy starting string
sample = "  AMD Ryzen   "

# Experiment 1: The trimmer
trimmed = sample.strip()
print("Trimmed version", trimmed)

# Experiment 2: The splitter
chopped = sample.split()
print("Chopped version", chopped)
print(f"First chopped part {chopped[0].strip()}")
print(f"Second chopped part {chopped[1].strip()}")

# 1. .strip() is a Trimmer ✂️
# It looks at one single string and shaves off any useless whitespace (spaces, tabs \t, or newlines \n) from the absolute far left and absolute far right.
# It does not touch the middle, and the result is still one single string.

# 2. .split() is an Axe 🪓
# It takes one single string and chops it into a List of multiple strings based on a separator.
# If you don't give it a separator, it chops wherever it sees a space.
