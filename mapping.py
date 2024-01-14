import detect_ayah
import line_detect
import support_class
import cv2
from model.glyph_model import Glyph
import pandas as pd
import index_to_data

# CSV
dataFrame = pd.DataFrame(columns=['page_number', 'index', 'line_number', 'sura_number', 'ayah_number', 'position',
                                  'min_x', 'min_y', 'max_x', 'max_y'])


########################################################################################################################
# all functions

def save_csv(gly, data_frame):
    new_row = pd.DataFrame({'page_number': [gly.page], 'index': [gly.index], 'line_number': [gly.line],
                            'sura_number': [gly.surah_number], 'ayah_number': [gly.ayah_number],
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
        left_top = [left_bottom[0], left_bottom[1] - 85]
        is_available = support_class.find_point_rectangle(left_top, right_bottom, uniq_detected_points[i])
        if is_available:
            cur_line_ayahs.append(uniq_detected_points[i])
            cur_line_ayahs = sorted(cur_line_ayahs, key=lambda x: (-x[0], x[0]))
    print(f'current_line_ayahs - {cur_line_ayahs}')

    aya_in_line = len(cur_line_ayahs)
    return aya_in_line, cur_line_ayahs


def line_position(line_no):
    r_b = [uniq_line_start_end_points[line_no - 1][1][0] + 10, uniq_line_start_end_points[line_no - 1][1][1]]
    r_t = [r_b[0], r_b[1] - 85]

    l_b = [uniq_line_start_end_points[line_no - 1][0][0] - 10, uniq_line_start_end_points[line_no - 1][0][1]]
    l_t = [l_b[0], l_b[1] - 85]

    # print('Right Top {}'.format(r_t))
    # print('Right Bottom {}'.format(r_b))
    # print(f'Left Top {l_t}')
    # print(f'Left Bottom {l_b}')

    return r_b, r_t, l_b, l_t


########################################################################################################################
# Main mapping logics
#######################################################################################################################

# start index & position
index = 5156
position = 1
start_page = 551
end_page = 605

for page in range(start_page, end_page + 1):
    print("#" * 200)
    print(f'page {page}')
    print("#" * 200)

    image_path = 'img/line_added_sample/page-{0:03d}.png'.format(page)
    img = cv2.imread(image_path, 0)

    # Ayah detected points
    uniq_detected_points, end_index = (
        detect_ayah.page_ayah_detect(image_path, index, 'test.png'))

    print("Ayah")
    print(len(uniq_detected_points))  # ayah detected in this page

    # line detected point
    uniq_line_start_end_points = line_detect.line_detect_points(image_path)
    uniq_line_start_end_points = sorted(uniq_line_start_end_points, key=lambda x: x[0][1])  # sorted lines Vertically(Y)

    print("Line")
    line_count = len(uniq_line_start_end_points)  # lines in this page
    print(line_count)
    print(uniq_line_start_end_points)

    # mapping etch line
    for line in range(1, line_count + 1):
        print("#" * (line * 5) + f"  Line {line}")

        ayah_in_line, current_line_ayahs = ayah_data_in_line(line)  # ayah count in line & start end point
        c_r_b, c_r_t, c_l_b, c_l_t = line_position(line)
        max_x = c_r_b[0]  # starting line before for loop
        max_y = c_r_b[1]
        # single line mapping
        for cur_ayah in current_line_ayahs:
            min_x = cur_ayah[0]
            min_y = c_l_t[1]

            surah_number, ayah_number = index_to_data.get_surah_ayah_no(index)
            glyph = Glyph(page, index, line, surah_number, ayah_number, position, min_x, min_y, max_x, max_y)

            # cv2.rectangle(img, (min_x, min_y), (max_x, max_y), (0, 0, 255), 2)
            # cv2.putText(img, 'pos {:d}'.format(position), (min_x, min_y), cv2.FONT_HERSHEY_SIMPLEX,
            #             1, (0, 0, 255), 2, cv2.LINE_AA)
            # cv2.putText(img, 'inx {:d}'.format(index), (min_x + 100, min_y), cv2.FONT_HERSHEY_SIMPLEX,
            #             2, (0, 0, 255), 1, cv2.LINE_AA)
            dataFrame = save_csv(glyph, dataFrame)

            max_x = cur_ayah[0]  # next starting
            max_y = c_r_b[1]
            index = index + 1
            position = 1

        # last part in line
        surah_number, ayah_number = index_to_data.get_surah_ayah_no(index)
        glyph = Glyph(page, index, line, surah_number, ayah_number, position, c_l_t[0], c_l_t[1], max_x, max_y)
        # cv2.rectangle(img, c_l_t, (max_x, max_y), (0, 0, 255), 2)
        # cv2.putText(img, 'pos {:d}'.format(position), (c_l_t[0], c_l_t[1] + 30), cv2.FONT_HERSHEY_SIMPLEX,
        #             1, (0, 0, 255), 2, cv2.LINE_AA)
        dataFrame = save_csv(glyph, dataFrame)
        position = position + 1

    print(index)
    # cv2.imshow(fr"img{page}", img)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
#######################################################################################################################
# save CSV file
dataFrame.to_csv("glyph.csv", index=True)
