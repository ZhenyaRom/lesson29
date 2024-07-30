class Horse:
    def __init__(self):
        self.x_distanse = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distanse += dx

class Eagle:
    def __init__(self):
        super().__init__()
        self.y_distanse = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distanse += dy

class Pegasus(Eagle, Horse):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        super().fly(dy)
        super().run(dx)


    def get_pos(self):
        return (self.x_distanse, self.y_distanse)

    def voice(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

