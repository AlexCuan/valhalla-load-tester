# import numpy as np
import random
from shapely.geometry import Polygon, Point

poly = Polygon([(23.109168639786912, -82.38050743782621), (23.08137764519128, -82.38977715218168),
                (23.0954317643179, -82.34600350105863), (23.112326343560625, -82.35750481331449)])


def polygon_random_points(poly, num_points):
    min_x, min_y, max_x, max_y = poly.bounds

    points = []

    while len(points) < num_points:
        random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if (random_point.within(poly)):
            points.append(random_point)
    return points
