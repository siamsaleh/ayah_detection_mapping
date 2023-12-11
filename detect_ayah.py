import cv2
import matplotlib.pyplot as plt
import numpy as np


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


def get_all_detected_point(loc):
    # all uniq point detected will be store here - tuple
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
            all_point_list = all_point_list + points_in_circle_np(25, point[0], point[1])  # add new circle all points
            print(point)
            # print(all_point_list)

    print(uniq_detected_points)
    print("All points - {:d}".format(len(detected_points)))
    print("Uniq ayah/points - {:d}".format(len(uniq_detected_points)))
    print("##########################################################")
    return uniq_detected_points


def template_matching():
    img_rgb = cv2.imread('sample/page-350.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('template/ayah_detect_trans.png', 0)
    h, w = template.shape[::]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    plt.imshow(res, cmap='gray')

    threshold = 0.5  # Pick only values above 0.8. For TM_CCOEFF_NORMED, larger values = good fit.

    loc = np.where(res >= threshold)
    uniq_detected_points = get_all_detected_point(loc)

    # Outputs 2 arrays. Combine these arrays to get x,y coordinates - take x from one array and y from the other.
    # Reminder: ZIP function is an iterator of tuples where first item in each iterator is paired together,
    # then the second item and then third, etc.
    for pt in uniq_detected_points:
        # cv2.circle(img_rgb, pt, 25, (0, 0, 255), 2)  # circle
        # Draw rectangle around each object. We know the top left (pt),
        # draw rectangle to match the size of the template image.
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 5)  # Red rectangles with thickness 2.

    # cv2.imwrite('images/template_matched.jpg', img_rgb)
    cv2.imshow("Matched image", img_rgb)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    template_matching()
