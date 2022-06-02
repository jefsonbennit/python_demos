# Program to generate a random number between 0 and 9

# importing the random module
import random
import time
from traceback import print_tb

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

while True:
    print(random.randint(0,9))
    print(time.time())
    time.sleep(5)
