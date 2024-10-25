# Python Data Structures: Stacks, Queues, and Sets

# Stacks
# A stack is a "Last In, First Out" (LIFO) data structure.
# In Python, we can use a list as a stack.

# Initialize an empty stack
stack = []

# Adding elements to the stack using append()
stack.append('A')  # Stack: ['A']
stack.append('B')  # Stack: ['A', 'B']
stack.append('C')  # Stack: ['A', 'B', 'C']

# Removing elements from the stack using pop()
last_item = stack.pop()  # Removes 'C'
print("Popped from stack:", last_item)  # Output: Popped from stack: C
print("Current stack:", stack)  # Output: Current stack: ['A', 'B']

# Queues
# A queue is a "First In, First Out" (FIFO) data structure.
# We can use the deque object from the collections module for efficient queue operations.

from collections import deque

# Initialize an empty queue
queue = deque()

# Adding elements to the queue using append()
queue.append('A')  # Queue: deque(['A'])
queue.append('B')  # Queue: deque(['A', 'B'])
queue.append('C')  # Queue: deque(['A', 'B', 'C'])

# Removing elements from the queue using popleft()
first_item = queue.popleft()  # Removes 'A'
print("Removed from queue:", first_item)  # Output: Removed from queue: A
print("Current queue:", queue)  # Output: Current queue: deque(['B', 'C'])

# Sets
# A set is an unordered collection of unique elements.
# Sets can be used to eliminate duplicates and ensure uniqueness.

# Create a set with some initial elements
unique_set = {1, 2, 3, 2, 1}  # Duplicates are ignored
print("Initial set:", unique_set)  # Output: Initial set: {1, 2, 3}

# Adding elements to the set
unique_set.add(4)
print("Set after adding 4:", unique_set)  # Output: Set after adding 4: {1, 2, 3, 4}

# Removing an element from the set
unique_set.remove(2)
print("Set after removing 2:", unique_set)  # Output: Set after removing 2: {1, 3, 4}

# Other Data Structures
# Default dictionaries can be used to provide default values for missing keys.
from collections import defaultdict

# Initialize a default dictionary with default value of 0
default_dict = defaultdict(int)

# Accessing a missing key returns the default value (0)
print("Default value for missing key 'nonexistent':", default_dict['nonexistent'])  # Output: 0

# Adding a value to a key
default_dict['existing'] += 1
print("Value for key 'existing':", default_dict['existing'])  # Output: 1

# Conclusion
# While Python has built-in support for several data structures,
# more complex structures like linked lists can be implemented as needed.
