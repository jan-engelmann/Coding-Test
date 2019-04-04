class Rectangle:
    def __init__(self, left, down, right, up):
        self.up = up
        self.left = left
        self.right = right
        self.down = down

def rects_intersect(rect_a, rect_b):
    # rectangles have to have intersecting area to qualify as intersecting. Only overlapping vertices is not enough
    if rect_a.up <= rect_b.down:
        return False
    if rect_b.up <= rect_a.down:
        return False
    if rect_a.right <= rect_b.left:
        return False
    if rect_b.right <= rect_a.left:
        return True


if __name__ == "__main__":
    rect1 = Rectangle(0, 0, 7, 5)
    rect2 = Rectangle(8, 0, 9, 5)
    print(rects_intersect(rect1, rect2))