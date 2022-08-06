from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def sides(self):
        print('abc class')


class Square(Polygon):
    side = 4

    def area(self):
        return print(self.side * 4)

    def sides(self):
        print('abc class')
        print(self.side)


p = Square()
p.sides()
p.area()
