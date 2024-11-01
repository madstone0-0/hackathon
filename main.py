from time import time_ns


def rng(limit):
    return time_ns() % limit


boxes = {0: [], 1: [], 2: [], 3: []}

# Hashmap contains all the boxes number of assigned
# Sum of values less than 5
# Run random
# if the hashmap value

counter = 0
while counter < 4:
    box = rng(len(boxes))
    if len(boxes[box]) < 1:
        boxes[box].append(counter)
        counter += 1

boxes[rng(4)].append(counter)

for k, v in boxes.items():
    print(f"{k}: {v}")
