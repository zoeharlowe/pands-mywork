# queue.py
# This program will put 10 random numbers into a queue (list)
# It will then output one number at a time and show the remaining numbers in the queue
# Author: Zoe McNamara Harlowe

import random

# Create an empty list called queue
queue = []

# While loop to add 10 random numbers to the list 'queue'
while len(queue) != 10:
    queue.append(random.randint(1,100))
print("queue is", queue)

# While loop to output one number at a time and show the remaining numbers in the queue
while len(queue) != 0:
    print("The current number is", queue.pop(0), "and the queue is", queue)
print("The queue is now empty")