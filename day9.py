class Point:
    def __init__(self, point):
        self.point = point

    def distance_to_origin(self):
        dis = 0
        for i in range(len(self.point)):
            dis += self.point[i]**2
        return dis**0.5


point_a = Point([1, 2])
point_b = Point([4, 5])
print(point_a.distance_to_origin())
print(point_b.distance_to_origin())
