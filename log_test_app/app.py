import logging
import random
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
)

# Example log messages
messages = [
    "User logged in successfully",
    "User failed authentication",
    "Payment processed",
    "Database connection error",
    "Cache miss",
    "File uploaded",
    "Email sent",
    "Timeout occurred",
]

# Loop to generate logs
while True:
    level = random.choice(["INFO", "WARNING", "ERROR"])
    msg = random.choice(messages)

    if level == "INFO":
        logging.info(msg)
    elif level == "WARNING":
        logging.warning(msg)
    else:
        logging.error(msg)

    time.sleep(random.uniform(0.5, 2.0))  # Random delay
