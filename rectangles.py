import math
import copy
# class with left, down, right, up already specified
class Rectangle_easy:
    def __init__(self, left, down, right, up):
        self.up = up
        self.left = left
        self.right = right
        self.down = down


# class with 4 x-y coordinates
class Rectangle_straight:
    def __init__(self, c0, c1, c2, c3):
        self.up = max(c0[1], c1[1], c2[1], c3[1])
        self.left = min(c0[0], c1[0], c2[0], c3[0])
        self.right = max(c0[0], c1[0], c2[0], c3[0])
        self.down = min(c0[1], c1[1], c2[1], c3[1])


def norm(vect):
    return math.sqrt(vect[0]**2 + vect[1]**2)

class Rectangle:
    def __init__(self, c0, c1, c2, c3):
        self.corners = [c0, c1, c2, c3]
        self.up = None
        self.left = None
        self.right = None
        self.down = None

    def straighten_around_point(self, point):

        y_coord = [c[1] for c in self.corners]

        indices = [i[0] for i in sorted(enumerate(y_coord), key=lambda x: x[1])]
        high = self.corners[indices[-1]]
        low = self.corners[indices[-2]]

        angle = math.acos((high[0] - low[0]) / math.sqrt((high[0] - low[0])**2 + (high[1] - low[1])**2)) - math.pi/2
        for i in range(4):
            self.corners[i] = self.rotate_point(self.corners[i], point, angle)

        y_coord = [c[1] for c in self.corners]
        x_coord = [c[0] for c in self.corners]

        self.up = max(y_coord)
        self.left = min(x_coord)
        self.right = max(x_coord)
        self.down = min(y_coord)

    def rotate_point(self, point, origin, angle):
            x = math.cos(angle) * (point[0] - origin[0]) - math.sin(angle) * (point[1] - origin[1]) + origin[0]
            y = math.sin(angle) * (point[0] - origin[0]) + math.cos(angle) * (point[1] - origin[1]) + origin[1]
            return x, y

    def point_in_rect(self, point):
        return point[0] < self.right and point[0] > self.left and point[1] < self.up and point[1] > self.down



def rects_intersect_basic(rect_a, rect_b):
    # rectangles have to have intersecting area to qualify as intersecting. Only overlapping vertices is not enough
    if rect_a.up <= rect_b.down:
        return False
    if rect_b.up <= rect_a.down:
        return False
    if rect_a.right <= rect_b.left:
        return False
    if rect_b.right <= rect_a.left:
        return False
    return True


def rects_intersect(rect_a, rect_b):
    for point in rect_b.corners:
        tmp_rect = copy.deepcopy(rect_a)
        tmp_rect.straighten_around_point(point)
        if tmp_rect.point_in_rect(point):
            return True
    return False

# Idee, wenn Rechtecke rotiert sein können: durch 4 ecken des einen Rechtecks iterieren, das andere um diesen Punkt gerade hindrehen, checken ob punkt zwischen den Bounds ist



if __name__ == "__main__":
    rect1 = Rectangle_easy(0, 0, 7, 5)
    rect2 = Rectangle_easy(8, 0, 9, 5)

    rect_a = Rectangle((0, 0), (0, 6), (8, 6), (8, 0))
    rect_b = Rectangle((1, 2), (1, 4), (5, 4), (5, 2))

    print(rects_intersect_basic(rect1, rect2))

    print(rects_intersect(rect_a, rect_b))

    rect_turn = Rectangle((-1, 0), (0, 1), (1, 0), (0, -1))
    rect_c = Rectangle((0.9, 0.9), (2, 0.9), (0.9, 3), (2, 3))
    print(rects_intersect(rect_turn, rect_c))