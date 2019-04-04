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
    def __str__(self):
        string = ""
        for el in self.corners:
            string += str(el) + '\n'
        return string
    # this method turns the rectangle by the specific angle so that its vertices are aligned with the axes
    def straighten_around_point(self, point):

        y_coord = [c[1] for c in self.corners]

        y_indices = [i[0] for i in sorted(enumerate(y_coord), key=lambda x: x[1])]
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
        return point[0] < self.right and point[0] > self.left and point[1] < self.up and point[1] > self.down


    # this is the mathematical formula for rotation of one point around a specified origin with an angle
def rotate_point(point, origin, angle):
        x = math.cos(angle) * (point[0] - origin[0]) - math.sin(angle) * (point[1] - origin[1]) + origin[0]
        y = math.sin(angle) * (point[0] - origin[0]) + math.cos(angle) * (point[1] - origin[1]) + origin[1]
        return x, y

# the algorithm checks for each corner of rect_b if it is inside rect_a
# 1. turn rect_a around point so that its vertices are parallel to the axes
# 2. check if point is inside the rectangle
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

    rect_c = Rectangle((-1, 0), (0, 1), (1, 0), (0, -1))
    rect_d = Rectangle((0.9, 0.9), (2, 0.9), (0.9, 3), (2, 3))
    print(rects_intersect(rect_c, rect_d))

    rect_e = Rectangle((-8.937, 6.718), (10.737, 3.118), (8.937, -6.718), (-10.737, -3.118))
    rect_f = Rectangle((60, 5), (12, 5), (60, 10), (12, 10))
    print(rects_intersect(rect_e, rect_f))