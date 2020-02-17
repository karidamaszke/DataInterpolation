class Spline:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = len(x)
        self.h = self.create_h()

    def create_h(self):
        h = []
        for i in range(self.size - 1):
            h.append(self.x[i + 1] - self.x[i])
        return h

    def create_a(self):
        pass

    def create_b(self):
        pass

    def spline(self):
        pass

    def draw(self):
        pass
