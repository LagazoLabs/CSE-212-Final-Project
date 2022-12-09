class MovieQueue:

    def __init__(self):
        self.queue = {}

    def enqueue(self, name, balance):
        self.queue[name] = balance

    def dequeue(self):
        if len(self.queue) <= 0:
            return None
        else:
            self.queue.pop(next(iter(self.queue)))

movie = MovieQueue()

movie.enqueue("Elsa", 5.99)
movie.enqueue("Dan", 6.99)
movie.enqueue("Marsha", 9.99)
movie.enqueue("David", 0.99)

#print(movie.queue)
print(next(iter(movie.queue)))
movie.dequeue()

#print(movie.queue)