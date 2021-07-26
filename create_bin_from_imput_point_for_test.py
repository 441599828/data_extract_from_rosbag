import numpy as np

points = np.array(
    [[17, 10, 3, 1], [17, 10, 0, 1], [10, 10, 3, 1], [10, 10, 0, 1], [17, -1, 3, 1], [17, -1, 1, 1], [10, -1, 3, 1],
     [10, -1, 1, 1]], dtype=np.float32)
file_name = './8_points.bin'
points.tofile(file_name)
