import detect_ayah
import line_detect
import support_class
import cv2
from model.glyph_model import Glyph
import pandas as pd

dataFrame = pd.DataFrame(columns=['page', 'index', 'line', 'position', 'min_x', 'min_y', 'max_x', 'max_y'])


########################################################################################################################


def save_csv(gly, data_frame):
    new_row = pd.DataFrame({'page': [gly.page], 'index': [gly.index], 'line': [gly.line],
                            'position': [gly.position], 'min_x': [gly.min_x], 'min_y': [gly.min_y],
                            'max_x': [gly.max_x], 'max_y': [gly.max_y]})
    return pd.concat([data_frame, new_row], ignore_index=True)


def ayah_data_in_line(line_no):
    ayah_in_page = len(uniq_detected_points)
    cur_line_ayahs = []
    for i in range(0, ayah_in_page):
        right_bottom = [uniq_line_start_end_points[line_no - 1][1][0] +
                        10, uniq_line_start_end_points[line_no - 1][1][1]]
        left_bottom = [uniq_line_start_end_points[line_no - 1][0][0] - 10,
                       uniq_line_start_end_points[line_no - 1][0][1]]
        left_top = [left_bottom[0], left_bottom[1] - 60]
        is_available = support_class.find_point_rectangle(left_top, right_bottom, uniq_detected_points[i])
        if is_available:
            cur_line_ayahs.append(uniq_detected_points[i])
            cur_line_ayahs = sorted(cur_line_ayahs, key=lambda x: (-x[0], x[0]))
    print(f'current_line_ayahs - {cur_line_ayahs}')

    aya_in_line = len(cur_line_ayahs)
    return aya_in_line, cur_line_ayahs


def line_position(line_no):
    r_b = [uniq_line_start_end_points[line_no - 1][1][0] + 10, uniq_line_start_end_points[line_no - 1][1][1]]
    r_t = [r_b[0], r_b[1] - 60]

    l_b = [uniq_line_start_end_points[line_no - 1][0][0] - 10, uniq_line_start_end_points[line_no - 1][0][1]]
    l_t = [l_b[0], l_b[1] - 60]

    # print('Right Top {}'.format(r_t))
    # print('Right Bottom {}'.format(r_b))
    # print(f'Left Top {l_t}')
    # print(f'Left Bottom {l_b}')

    return r_b, r_t, l_b, l_t


########################################################################################################################

# print("#" * 200)
#
# page = 2
#
# image_path = 'img/surah_border_less_sample/page-{0:03d}.png'.format(page)
# img = cv2.imread(image_path, 0)

# Ayah detected points
next_page_start = 0
uniq_detected_points, end_index = (
    detect_ayah.page_ayah_detect(image_path, next_page_start, 'test.png'))

print("Ayah")
print(len(uniq_detected_points))
# print(uniq_detected_points)
# for point in uniq_detected_points:
#     print(point)

# line detected point
uniq_line_start_end_points = line_detect.line_detect_points(image_path)
uniq_line_start_end_points = sorted(uniq_line_start_end_points, key=lambda x: x[0][1])

print("Line")
line_count = len(uniq_line_start_end_points)
print(line_count)
print(uniq_line_start_end_points)

##########################################################################

# line 2
# line_no = 14

# right_bottom = [uniq_line_start_end_points[line_no - 1][1][0] + 10, uniq_line_start_end_points[line_no - 1][1][1]]
# right_top = [right_bottom[0], right_bottom[1] - 60]
#
# left_bottom = [uniq_line_start_end_points[line_no - 1][0][0] - 10, uniq_line_start_end_points[line_no - 1][0][1]]
# left_top = [left_bottom[0], left_bottom[1] - 60]

# TODO all points in this rectangle
# is_available = support_class.find_point_rectangle(left_top, right_bottom, uniq_detected_points[3])
# print(uniq_detected_points[3])
# print(is_available)

# mappings = []

# TODO sort line points (Get All Ayah in this line)
# ayah_in_page = len(uniq_detected_points)
# current_line_ayahs = []
# for i in range(0, ayah_in_page):
#     is_available = support_class.find_point_rectangle(left_top, right_bottom, uniq_detected_points[i])
#     if is_available:
#         current_line_ayahs.append(uniq_detected_points[i])
#         current_line_ayahs = sorted(current_line_ayahs, key=lambda x: (-x[0], x[0]))
# print(f'current_line_ayahs - {current_line_ayahs}')
#
# ayah_in_line = len(current_line_ayahs)

# mapping one line
# index = 0
# position = 1
#
# # ayah start from line end in line
# min_x = current_line_ayahs[0][0]
# min_y = left_top[1]
# max_x = right_bottom[0]
# max_y = right_bottom[1]
# glyph = Glyph(index, position, min_x, min_y, max_x, max_y)
# mappings.append(glyph)
# glyph.print_values()
# index = index + 1

# ayah start from middle - end in middle

# ayah start but not end in line

# ayah start in previous line - end here

# ayah start previous line end next line
#######################################################################################################################

index = 0
position = 1


for page in range(2, 100):

    for line in range(1, line_count+1):

        print("#" * (line*5) + f"  Line {line}")
        ayah_in_line, current_line_ayahs = ayah_data_in_line(line)
        c_r_b, c_r_t, c_l_b, c_l_t = line_position(line)
        max_x = c_r_b[0]  # starting line before for loop
        max_y = c_r_b[1]

        for cur_ayah in current_line_ayahs:
            min_x = cur_ayah[0]
            min_y = c_l_t[1]

            glyph = Glyph(page, index, line, position, min_x, min_y, max_x, max_y)
            # mappings.append(glyph)

            cv2.rectangle(img, (min_x, min_y), (max_x, max_y), (0, 0, 255), 2)
            cv2.putText(img, 'pos {:d}'.format(position), (min_x, min_y), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2, cv2.LINE_AA)
            dataFrame = save_csv(glyph, dataFrame)

            max_x = cur_ayah[0]  # next starting
            max_y = c_r_b[1]
            index = index + 1
            position = 1

        # last part in line
        glyph = Glyph(page, index, line, position, c_l_t[0], c_l_t[1], max_x, max_y)
        cv2.rectangle(img, c_l_t, (max_x, max_y), (0, 0, 255), 2)
        cv2.putText(img, 'pos {:d}'.format(position), (c_l_t[0], c_l_t[1] + 30), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 2, cv2.LINE_AA)
        dataFrame = save_csv(glyph, dataFrame)
        position = position + 1

#######################################################################################################################
# TODO make rectangle of every ayah
# cv2.rectangle(img, left_top, right_bottom, (0, 0, 255), 5)


# cv2.rectangle(img, (min_x, min_y), (max_x, max_y), (0, 0, 255), 5)  # Red rectangles with thickness 2.
# cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()

# Create a new DataFrame with a single row
# new_row = pd.DataFrame({'page_no': [1], 'line': [2], 'position': [3], 'ayah': [4]})
# dataFrame = pd.concat([dataFrame, new_row], ignore_index=True)

dataFrame.to_csv("glyph.csv", index=True)
