import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Process CUSTOMER, IMAGE, and EMAIL details.")
parser.add_argument("--CUSTOMER", type=str, required=True, help="Customer name")
parser.add_argument("--IMAGE", type=str, required=True, help="Image name")
parser.add_argument("--EMAIL", type=str, required=True, help="Email address")

# Parse the arguments
args = parser.parse_args()

# Access the arguments
customer = args.CUSTOMER
image = args.IMAGE
email = args.EMAIL

# Print "Hello, World!"
print("Hello, World!")

# Print the message with the passed arguments
print(f"And I waited for 10 secs. Arguments passed: CUSTOMER={customer}, IMAGE={image}, EMAIL={email}")
