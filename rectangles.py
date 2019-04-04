# class with left, down, right, up already specified
class Rectangle_easy:
    def __init__(self, left, down, right, up):
        self.up = up
        self.left = left
        self.right = right
        self.down = down


# class with 4 x-y coordinates
class Rectangle:
    def __init__(self, c0, c1, c2, c3):
        self.up = max(c0[1], c1[1], c2[1], c3[1])
        self.left = min(c0[0], c1[0], c2[0], c3[0])
        self.right = max(c0[0], c1[0], c2[0], c3[0])
        self.down = min(c0[1], c1[1], c2[1], c3[1])


def rects_intersect(rect_a, rect_b):
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



if __name__ == "__main__":
    rect1 = Rectangle_easy(0, 0, 7, 5)
    rect2 = Rectangle_easy(8, 0, 9, 5)

    rect_a = Rectangle((0, 0), (0, 6), (8, 6), (8, 0))
    rect_b = Rectangle((1, 2), (1, 4), (5, 4), (5, 2))

    print(rects_intersect(rect1, rect2))

    print(rects_intersect(rect_a, rect_b))
