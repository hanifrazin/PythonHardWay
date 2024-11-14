import random


def coords_generator(n = 5):
    coords = []
    for _ in range (0,n):
        coords.append({
            "x" : random.randint(-5,5),
            "y" : random.randint(-5,5)
        })
    return coords

data = coords_generator(8)
for c in data:
    match c:
        case {"x": 0, "y": 0}:
            print(f"coord {c} is positioned at the center")
        case {"x": x, "y": 0} if x < 0:
            print(f"coord {c} is positioned at the left horizontally center")
        case {"x": x, "y": 0} if x > 0:
            print(f"coord {c} is positioned at the right horizontally center")
        case {"x": 0, "y": y} if y < 0:
            print(f"coord {c} is positioned at the bottom vertically center")
        case {"x": 0, "y": y} if y > 0:
            print(f"coord {c} is positioned at the top vertically center")
        case {"x": -5, "y": 5} | {"x": -5, "y": -5} | {"x": 5, "y": -5} | {"x": 5, "y": 5}:
            print(f"coord {c} is positioned at certain corner")
        case other:
            print(f"coord {other} is positioned at the somewhere")