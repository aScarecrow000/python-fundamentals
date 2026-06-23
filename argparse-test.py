import argparse

# create the parser
arg_parser = argparse.ArgumentParser(description="This is a test script for argparse.")
arg_parser.add_argument("mau", help="This is the main argument.")
# recall the arguments
arg_parser.parse_args()
args = arg_parser.parse_args()

print(f"The value of the main argument 'mau' is: {args.mau}")
