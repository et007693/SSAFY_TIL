class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_info(self):
        print(f'Width: {self.width}')
        print(f'Height: {self.height}')
        print(f'Area: {self.height * self.width}')
        print(f'Perimeter: {(self.height+self.width) * 2}')

shape1 = Shape(5, 3)
shape1.print_info()
