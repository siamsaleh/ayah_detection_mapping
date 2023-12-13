import os
import numpy as np


def get_file_names(folder_path, add_pre_text):
    file_names = []
    # List all files in the folder
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_names.append(add_pre_text + filename)  # file name

    return file_names


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


# def is_point_available_rectangle(bottom_left, top_right, point):
#     if (bottom_left[0] < point[0] < top_right[0] and point[1] > bottom_left[1] and point[1] < top_right[1]):
#         return True
#     else:
#         return False
#
#
# def point_in_rectangle(point, rect):
#     x1, y1, w, h = rect
#     x2, y2 = x1 + w, y1 + h
#     x, y = point
#     if (x1 < x and x < x2):
#         if (y1 < y and y < y2):
#             return True
#     return False
#
#
# def find_point(x1, y1, x2, y2, x, y):
#     if x1 < x < x2 and y1 < y < y2:
#         return True
#     else:
#         return False


def find_point_rectangle(left_top, right_bottom, point):
    if left_top[0] < point[0] < right_bottom[0] and left_top[1] < point[1] < right_bottom[1]:
        return True
    else:
        return False
