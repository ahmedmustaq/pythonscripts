import os
import time

# Access environment variables
customer = os.getenv("CUSTOMER", "default_customer")  # Default value if CUSTOMER is not set
image = os.getenv("IMAGE", "default_image")          # Default value if IMAGE is not set

# Motivational Quote Program
print("Believe you can and you're halfway there.")

# Print the second message with environment variables
print(f"Environment variables: CUSTOMER={customer}, IMAGE={image}")
