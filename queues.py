"""
A scripted way to implement a queue. Contains all the relevant methods for a queue: enqueue, dequeue, check_empty,
check_full, check_size
"""

new_queue = [None, None, None, None, None, None]

front_pointer = 0
end_pointer = 0

# Add an item to a queue (enqueue)
new_value = "John Benson"
new_queue[end_pointer] = new_value
end_pointer += 1

# Enqueue
new_value = "Ben Johnson"
new_queue[end_pointer] = new_value
end_pointer += 1

# Read item from the front of the queue (dequeue)
dequeued_item = new_queue[front_pointer]
front_pointer += 1

# Find size of the queue
size_of_queue = end_pointer - front_pointer

# Check if queue is empty
if size_of_queue == 0:
    print("Queue is empty")
else:
    print("Queue is not empty")

# Check if queue is full
if end_pointer - 1 == len(new_queue):
    print("Queue is full")
else:
    print("Queue is not full")

