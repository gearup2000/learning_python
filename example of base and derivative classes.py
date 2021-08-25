class Base:
    def __init__(self, x):
        self.x = x

    def show(self):
        print('Base', self.x)


class Derivative(Base):
    def __init__(self):
        super().__init__(20)
        # Base.__init__(self, 20) wrong way of getting data from parent class.
        # Or in case there is many parents could be applied.
        self.name = ''


a = Base(10)
b = Derivative()
a.show()
b.show()
