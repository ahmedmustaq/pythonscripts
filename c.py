import os
import time

# Access environment variables
customer = os.getenv("CUSTOMER", "default_customer")  # Default value if CUSTOMER is not set
image = os.getenv("IMAGE", "default_image")          # Default value if IMAGE is not set
email = os.getenv("CUSTOMER_EMAIL", "a@b.com")          # Default value if IMAGE is not set

# Print "Hello, World!"
print("Hello, World!")

# Print the second message with environment variables
print(f"And I waited for 10 secs. Environment variables: CUSTOMER={customer}, IMAGE={image},CUSTOMER_EMAIL={email}")
