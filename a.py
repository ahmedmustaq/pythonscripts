import argparse
import os

# Set up argument parser
parser = argparse.ArgumentParser(description="Process URL details.")
parser.add_argument("--URL", type=str, help="URL name (can also be set as an environment variable 'URL')")

# Parse the arguments
args = parser.parse_args()

# Check if URL is provided as an argument or environment variable
url = args.URL or os.getenv("URL")

# Validate that URL is provided
if not url:
    print("Error: URL must be provided either as an argument (--URL) or as an environment variable 'URL'.")
    exit(1)

# Print "Hello, World!"
print("Hello, World!")

# Print the message with the URL value
print(f"And I waited for 10 secs. URL={url}")
