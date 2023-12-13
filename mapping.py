import detect_ayah
import line_detect
import support_class
import cv2

image_path = 'img/surah_border_less_sample/page-602.png'

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
line_no = 2

right_bottom = [uniq_line_start_end_points[line_no - 1][1][0], uniq_line_start_end_points[line_no - 1][1][1]]
right_top = [right_bottom[0], right_bottom[1] - 60]

left_bottom = [uniq_line_start_end_points[line_no - 1][0][0], uniq_line_start_end_points[line_no - 1][0][1]]
left_top = [left_bottom[0], left_bottom[1] - 60]

print(right_top)
print(right_bottom)
print(left_top)
print(left_bottom)

# TODO all points in this rectangle
is_available = support_class.find_point_rectangle(left_top, right_bottom, uniq_detected_points[3])
print(uniq_detected_points[3])
print(is_available)

# TODO sort line points

# TODO make rectangle of every ayah

# img = cv2.imread(image_path, 0)
# cv2.rectangle(img, left_top, right_bottom, (0, 0, 255), 5)  # Red rectangles with thickness 2.
# cv2.imshow("img", img)
# cv2.waitKey()
# cv2.destroyAllWindows()

