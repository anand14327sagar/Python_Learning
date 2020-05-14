import queue
q1 = queue.Queue(6)
q1.put(1)
q1.put(2)
q1.put(3)
q1.put(4)
q1.put(5)
print(q1.full())

# q1 = queue.Queue()
q1 = queue.LifoQueue()
q1.put(10)
item1 = q1.get()
print('The item removed from the queue is ', item1)