from util import readgroups, readgrid

*shapes, areas = readgroups()

shapes = [readgrid(shape) for _shape_idx, *shape in shapes]

areas = [
    (tuple(map(int, area.split(": ")[0].split("x"))), tuple(map(int, area.split(": ")[1].split()))) for area in areas
]

shape_areas = {i: "".join("".join(row) for row in shape).count("#") for i, shape in enumerate(shapes)}

print(sum(1 for (w, h), shape_req in areas if w * h >= sum(n * shape_areas[i] for i, n in enumerate(shape_req))))
