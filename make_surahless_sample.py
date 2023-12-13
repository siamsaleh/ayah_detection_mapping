import cv2
import matplotlib.pyplot as plt
import numpy as np
import support_class


def get_all_detected_point(loc):
    uniq_detected_points = []
    # all TEMPLATE MATCHING points
    detected_points = []  # this will be a list and the items will be tuple
    for pt in zip(*loc[::-1]):
        detected_points.append(pt)

    all_point_list = []  # type list
    for point in detected_points:
        if point in all_point_list:
            # exist pass
            pass
        else:
            # not exist
            uniq_detected_points.append(point)  # if not exist it is uniq point
            # add new circle all points
            all_point_list = all_point_list + support_class.points_in_circle_np(25, point[0], point[1])
            print(point)
            # print(all_point_list)

    print(uniq_detected_points)
    print("All points - {:d}".format(len(detected_points)))
    print("Uniq ayah/points - {:d}".format(len(uniq_detected_points)))
    print("##########################################################")
    return uniq_detected_points


def template_matching(image_path, start_index, save_file_name):
    img_rgb = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('template/surah_start_detect.png', 0)
    h, w = template.shape[::]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    plt.imshow(res, cmap='gray')

    threshold = 0.5  # Pick only values above 0.8. For TM_CCOEFF_NORMED, larger values = good fit.

    loc = np.where(res >= threshold)
    uniq_detected_points = get_all_detected_point(loc)

    if (len(uniq_detected_points) > 0):
        for pt in uniq_detected_points:
            # cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 5)  # Red rectangles with thickness 2.
            # cv2.putText(img_rgb, 'Ayah Index {:d}'.format(start_index), pt, cv2.FONT_HERSHEY_SIMPLEX,
            #             1, (255, 0, 0), 2, cv2.LINE_AA)

            h_plus = 34
            cv2.line(img_rgb, (pt[0], pt[1] + h_plus), (pt[0] + w, pt[1] + h_plus), (255, 255, 255), 70)
            print(pt)
            print(h)
            start_index = start_index + 1

    cv2.imwrite('img/surah_border_less_sample/' + save_file_name, img_rgb)

    # cv2.imshow("Matched image", img_rgb)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    print(image_path)
    print("###########################################################################################################")
    return uniq_detected_points, start_index


def surah_detect(image_path, start_index, save_file_name):
    uniq_detected_points, end_index = template_matching(image_path, start_index, save_file_name)
    return uniq_detected_points, end_index


#######################################################################################################################
all_file_names = support_class.get_file_names("borderless_sample/", "")
image_count = len(all_file_names)
print(image_count)

next_page_start = 1
for i in range(0, image_count):
    save_file_name = 'page-{0:03}.png'.format(i + 1)
    image_path = 'borderless_sample/' + save_file_name
    uniq_detected_points, end_index = (
        surah_detect(image_path, next_page_start, save_file_name))
    next_page_start = end_index

print(next_page_start)

# uniq_detected_points, end_index = (
#         surah_detect('borderless_sample/page-446.png', 0, 'test.png'))
