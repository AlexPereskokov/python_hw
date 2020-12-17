class Road:
    __length = None
    __width = None
    weigth = None
    tickness = None

    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('Your sizes has been entered')

    def mass(self):
        self.weigth = 25
        self.tickness = 0.05
        asf_mass = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'Need {asf_mass} ton for road implementation ')


mas_our_road = Road(20, 5000)
mas_our_road.mass()
