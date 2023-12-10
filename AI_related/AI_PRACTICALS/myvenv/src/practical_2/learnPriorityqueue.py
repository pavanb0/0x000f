import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, item))

    def pop(self):
        if not self.is_empty():
            return heapq.heappop(self._queue)[1]
        else:
            raise IndexError("pop from an empty priority queue")

    def is_empty(self):
        return len(self._queue) == 0

# Example Usage:
priority_queue = PriorityQueue()

priority_queue.push("Task 1", 3)
priority_queue.push("Task 2", 1)
priority_queue.push("Task 3", 2)

while not priority_queue.is_empty():
    print(priority_queue.pop())
