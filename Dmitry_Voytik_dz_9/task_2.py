class Road:
    def __init__(self, width, length):
        self._length = length
        self._width = width

    def total_calcs(self, mass=25, thickness=5):
        return (f"{self._width} m * {self._length} m * {mass} kilo * {thickness} cm = "
                f"{self._width * self._length * mass * thickness / 1000} tonns")


# width 20 m, length 5000 m (script)
best_road_ever = Road(int(input('Enter Road width in m: ')), int(input('Enter Road length in m: ')))
print(best_road_ever.total_calcs())
