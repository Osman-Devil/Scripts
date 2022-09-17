class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def calc_asphalt_mass(self, asphalt_mass=25, asphalt_thickness=5):
        return str((self._length * self._width * asphalt_mass * asphalt_thickness) / 1000) + " тон"


a = Road(20, 5000)
print(a.calc_asphalt_mass())
