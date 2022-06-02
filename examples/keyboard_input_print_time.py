# Program to generate a random number between 0 and 9

# importing the random module
import random
import time
from traceback import print_tb

from datetime import datetime


while True:
    print(random.randint(0,9))
    print(time.time())
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    print("Please enter some text : ")
    input1 = input()
    print("================== You entered : ",input1)
    
    fruits = ["apple", "banana", "cherry"]
    try:
        print("Printing fruits[0] : ",fruits[0])
        print("Printing fruits[2] : ",fruits[2])
        print("Printing fruits[3] : ",fruits[3])
    except:
        print("problem with my code")