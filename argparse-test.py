import argparse

# 1. Create the master parser
mau = argparse.ArgumentParser()

# 2. Register the arguments (slots) here
mau.add_argument("echo", help="echo the string you use here")
mau.add_argument(
    "--square", help="gives you the sqaure of the number you use here", type=int
)  # making it optional with --square
mau.add_argument(
    "--verbose", help="increase output verbosity", action="store_true"
)  # adding a flag for verbosity, a true/false switch

# 3. Parse the arguments
args = mau.parse_args()

# 4. Use conditions to run my practice blocks
print(f"echo argument parse: {args.echo}")

if args.square is not None:
    print(f"square argument parse: {args.square**2}")
if args.verbose:
    print("verbosity turned on")
