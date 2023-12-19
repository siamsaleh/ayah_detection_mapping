import os
import numpy as np


def get_file_names(folder_path, add_pre_text):
    file_names = []
    # List all files in the folder
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_names.append(add_pre_text + filename)  # file name

    return file_names


# all points in circle
# circle center (x0, y0)
def points_in_circle_np(radius, x0, y0):
    x_ = np.arange(x0 - radius - 1, x0 + radius + 1, dtype=int)
    y_ = np.arange(y0 - radius - 1, y0 + radius + 1, dtype=int)
    x, y = np.where((x_[:, np.newaxis] - x0) ** 2 + (y_ - y0) ** 2 <= radius ** 2)
    # x, y = np.where((np.hypot((x_-x0)[:,np.newaxis], y_-y0)<= radius)) # alternative implementation
    all_point_list = []
    for x, y in zip(x_[x], y_[y]):
        point = (x, y)
        all_point_list.append(point)
    return all_point_list


# all points in a rectangle
# Top-left corner (x1, y1)
# Bottom-right corner (x2, y2)
def get_integer_points_in_rectangle(x1, y1, x2, y2):
    points = []
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            points.append((x, y))
    return points


# is the point is available in this rectangle or not
def find_point_rectangle(left_top, right_bottom, point):
    if left_top[0] < point[0] < right_bottom[0] and left_top[1] < point[1] < right_bottom[1]:
        return True
    else:
        return False
