from collections import deque

MAX_SIZE = 100  # Maximum size of the list
data = deque(maxlen=MAX_SIZE)

# Adding elements to the list
for i in range(1000):
    data.append(i)

# The list will only contain the last 100 elements
print(len(data))  # Output: 100
