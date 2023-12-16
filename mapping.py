import detect_ayah
import line_detect
import support_class
import cv2
from model.glyph_model import Glyph
import pandas as pd

dataFrame = pd.DataFrame(columns=['page', 'index', 'line', 'position', 'min_x', 'min_y', 'max_x', 'max_y'])

page = 602

image_path = 'img/surah_border_less_sample/page-{0:03d}.png'.format(page)
img = cv2.imread(image_path, 0)

# Ayah detected points
next_page_start = 0
uniq_detected_points, end_index = (
    detect_ayah.page_ayah_detect(image_path, next_page_start, 'test.png'))

print("Ayah")
print(len(uniq_detected_points))
# print(uniq_detected_points)
for point in uniq_detected_points:
    print(point)

print("################")

# line detected point
uniq_line_start_end_points = line_detect.line_detect_points(image_path)
uniq_line_start_end_points = sorted(uniq_line_start_end_points, key=lambda x: x[0][1])

print("Line")
print(len(uniq_line_start_end_points))
print(uniq_line_start_end_points)

# line 2
line_no = 14

right_bottom = [uniq_line_start_end_points[line_no - 1][1][0] + 10, uniq_line_start_end_points[line_no - 1][1][1]]
right_top = [right_bottom[0], right_bottom[1] - 60]

left_bottom = [uniq_line_start_end_points[line_no - 1][0][0] - 10, uniq_line_start_end_points[line_no - 1][0][1]]
left_top = [left_bottom[0], left_bottom[1] - 60]

print('Right Top {}'.format(right_top))
print('Right Bottom {}'.format(right_bottom))
print(f'Left Top {left_top}')
print(f'Left Bottom {left_bottom}')

# TODO all points in this rectangle
# is_available = support_class.find_point_rectangle(left_top, right_bottom, uniq_detected_points[3])
# print(uniq_detected_points[3])
# print(is_available)

mappings = []

# TODO sort line points (Get All Ayah in this line)
ayah_in_page = len(uniq_detected_points)
current_line_ayahs = []
for i in range(0, ayah_in_page):
    is_available = support_class.find_point_rectangle(left_top, right_bottom, uniq_detected_points[i])
    if is_available:
        current_line_ayahs.append(uniq_detected_points[i])
        current_line_ayahs = sorted(current_line_ayahs, key=lambda x: (-x[0], x[0]))
print(f'current_line_ayahs - {current_line_ayahs}')

ayah_in_line = len(current_line_ayahs)

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
index = 0
position = 1
is_ayah_finish = False
max_x = right_bottom[0]  # starting line before for loop
max_y = right_bottom[1]

for line in range(1, 15):

    for cur_ayah in current_line_ayahs:
        min_x = cur_ayah[0]
        min_y = left_top[1]

        glyph = Glyph(page, index, line_no, position, min_x, min_y, max_x, max_y)
        mappings.append(glyph)

        cv2.rectangle(img, (min_x, min_y), (max_x, max_y), (0, 0, 255), 5)
        new_row = pd.DataFrame({'page': [glyph.page], 'index': [glyph.index], 'line': [glyph.line],
                                'position': [glyph.position], 'min_x': [glyph.min_x], 'min_y': [glyph.min_y],
                                'max_x': [glyph.max_x], 'max_y': [glyph.max_y]})
        dataFrame = pd.concat([dataFrame, new_row], ignore_index=True)

        max_x = cur_ayah[0]  # next starting
        max_y = right_bottom[1]
        index = index + 1
        # position = 0

# TODO make rectangle of every ayah
# cv2.rectangle(img, left_top, right_bottom, (0, 0, 255), 5)


# cv2.rectangle(img, (min_x, min_y), (max_x, max_y), (0, 0, 255), 5)  # Red rectangles with thickness 2.
cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()

# Create a new DataFrame with a single row
# new_row = pd.DataFrame({'page_no': [1], 'line': [2], 'position': [3], 'ayah': [4]})
# dataFrame = pd.concat([dataFrame, new_row], ignore_index=True)

dataFrame.to_csv("glyph.csv", index=True)
