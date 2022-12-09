class MoveTicketqueue:

    def __init__(self):
        self.queue = []

    def get_current_queue(self):
        return self.queue

    def get_queue_size(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def purchase_ticket(self):
        value = self.queue[0] 
        del self.queue[0]
        return value

avengers_endgame = MoveTicketqueue()

avengers_endgame.enqueue("Alison")
avengers_endgame.enqueue("Adison")
avengers_endgame.enqueue("Madison")
avengers_endgame.enqueue("Jamison")
avengers_endgame.enqueue("Benson")
avengers_endgame.enqueue("Lilly")
avengers_endgame.enqueue("Billy")
avengers_endgame.enqueue("Milly")

print(avengers_endgame.get_current_queue())

print(avengers_endgame.get_current_queue())

avengers_endgame.purchase_ticket()
print(avengers_endgame.get_current_queue())

avengers_endgame.purchase_ticket()
print(avengers_endgame.get_current_queue())

avengers_endgame.purchase_ticket()
print(avengers_endgame.get_current_queue())

avengers_endgame.purchase_ticket()
print(avengers_endgame.get_current_queue())

avengers_endgame.purchase_ticket()
print(avengers_endgame.get_current_queue())

avengers_endgame.purchase_ticket()
print(avengers_endgame.get_current_queue())

avengers_endgame.purchase_ticket()
print(avengers_endgame.get_current_queue())

avengers_endgame.purchase_ticket()
print(avengers_endgame.get_current_queue())

avengers_endgame.purchase_ticket()
print(avengers_endgame.get_current_queue())