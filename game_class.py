class Game:
    def __init__(self):
        self.number = '1234'

    # @property
    def __new__(cls):
        if hasattr(cls, 'instance'):
            pass
        else:
            cls.instance = super(Game, cls).__new__(cls)
        return cls.instance

    def check_bulls(self, hypothesis):
        bulls = 0
        for i in range(len(self.number)):
            if self.number[i] == hypothesis[i]:
                bulls += 1
        return bulls

    def check_cows(self, hypothesis):
        pass
