import math
import copy


class Rectangle:
    # initialize arbitrary rectangle with corners (x,y)
    def __init__(self, c0, c1, c2, c3):
        self.corners = [c0, c1, c2, c3]
        # the following values will be initialized in the method straighten_around_point
        self.up = None
        self.left = None
        self.right = None
        self.down = None

    # this method turns the rectangle by the specific angle so that its vertices are aligned with the axes
    def straighten_around_point(self, point):

        y_coord = [c[1] for c in self.corners]
        y_indices = [i[0] for i in sorted(enumerate(y_coord), key=lambda x: x[1])]

        # use the upper two points to determine the angle towards the axes
        high = self.corners[y_indices[-1]]
        low = self.corners[y_indices[-2]]

        angle = math.acos((high[0] - low[0]) / math.sqrt((high[0] - low[0])**2 + (high[1] - low[1])**2)) - math.pi/2
        for i in range(4):
            self.corners[i] = rotate_point(self.corners[i], point, angle)

        y_coord = [c[1] for c in self.corners]
        x_coord = [c[0] for c in self.corners]

        self.up = max(y_coord)
        self.left = min(x_coord)
        self.right = max(x_coord)
        self.down = min(y_coord)

        return angle

    # this formula only works if the rectangle is straightened
    def point_in_rect(self, point):
        return self.left < point[0] < self.right and self.down < point[1] < self.up


# this is the mathematical formula for rotation of one point around a specified origin with an angle
def rotate_point(point, origin, angle):
        x = math.cos(angle) * (point[0] - origin[0]) - math.sin(angle) * (point[1] - origin[1]) + origin[0]
        y = math.sin(angle) * (point[0] - origin[0]) + math.cos(angle) * (point[1] - origin[1]) + origin[1]
        return x, y


# the algorithm checks for each corner of rect_b if it is inside rect_a
# 1. turn rect_a around origin so that its vertices are parallel to the axes
# 2. turn point as well around origin for the same angle
# 3. check if point is inside the rectangle
def rects_intersect(rect_a, rect_b):
    for point in rect_b.corners:
        tmp_rect = copy.deepcopy(rect_a)
        angle = tmp_rect.straighten_around_point((0,0))
        point = rotate_point(point, (0,0), angle)
        if tmp_rect.point_in_rect(point):
            return True
    return False


if __name__ == "__main__":
    rect_a = Rectangle((0, 0), (0, 6), (8, 6), (8, 0))
    rect_b = Rectangle((1, 2), (1, 4), (5, 4), (5, 2))
    print(rects_intersect(rect_a, rect_b))

    coord_c = (-1, 0), (0, 1), (1, 0), (0, -1)
    coord_d = (0.6, 0.6), (1, 1), (1.4, 0.6), (1, 0.2)
    rect_c = Rectangle(*coord_c)
    rect_d = Rectangle(*coord_d)
    print(rects_intersect(rect_c, rect_d))

    # visualization of the rectangles
    import matplotlib.pyplot as plt
    x = [el[0] for el in coord_d]
    y = [el[1] for el in coord_d]

    xb = [el[0] for el in coord_c]
    yb = [el[1] for el in coord_c]

    plt.figure()
    plt.scatter(x, y)
    plt.scatter(xb, yb)
    plt.fill(x, y)
    plt.fill(xb, yb)
    plt.axis('equal')
    plt.show()
