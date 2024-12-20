import random

def coords_generator(n = 5):
    coords = []
    for _ in range(n):
        coords.append((random.randint(-5,5), random.randint(-5,5)))
    return coords

data = coords_generator(8)
for c in data:
    match c:
        case(0, 0):
            print(f"coord {c} is positioned at the center")
        case(x, 0) if x < 0:
            print(f"coord {c} is positioned at the left horizontally center")
        case(x, 0) if x > 0:
            print(f"coord {c} is positioned at the right horizontally center")
        case(0, y) if y < 0:
            print(f"coord {c} is positioned at the bottom vertically center")
        case(0, y) if y > 0:
            print(f"coord {c} is positioned at the top vertically center")
        case(-5, 5) | (-5, -5) | (5, -5) | (5, 5):
            print(f"coord {c} is positioned at certain corner")
        case other:
            print(f"coord {other} is positioned at the somewhere")