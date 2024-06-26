import threading
from game.ai import AlphaBetaPruner

class Brain(threading.Thread):
    def __init__(self, duration, mutex, q, pieces, first_player, second_player):
        self.mutex = mutex
        self.q = q
        self.duration = duration
        self.pieces = pieces
        self.first_player = first_player
        self.second_player = second_player
        self.has_started = False
        self.lifetime = None
        threading.Thread.__init__(self)

    def run(self):
        pruner = AlphaBetaPruner(self.mutex, self.duration, self.pieces, self.first_player, self.second_player)
        result = pruner.alpha_beta_search()
        self.q.put(result)

