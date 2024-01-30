from scipy import interpolate
import numpy as np


def b_spline(waypoints, num=50):
    x = []
    y = []

    for waypoint in waypoints:
        x.append(waypoint[0])
        y.append(waypoint[1])

    tck, *rest = interpolate.splprep([x, y])

    u = np.linspace(0, 1, num=num)
    smooth = interpolate.splev(u, tck)

    return [(x, y) for x, y in zip(smooth[0], smooth[1])]
