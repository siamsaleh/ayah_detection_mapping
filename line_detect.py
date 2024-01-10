import cv2
import numpy as np
import support_class


def line_detect_points(image_path, save_file_name="test/line.png"):
    # img = cv2.imread('borderless_sample/page-051.png')
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 200, minLineLength=790, maxLineGap=40)  # 584 580 900

    uniq_line_start_end_points = []  # [(x1, y1), (x2, y2)]

    x = 0
    all_start_point_list = []

    if lines is None:
        pass
    else:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            # start_pt = (x1 + 25, y1)
            # end_pt = (x2 - 25, y2)
            start_pt = (x1, y1)
            end_pt = (x2, y2)
            # cv2.line(img, start_pt, end_pt, (0, 0, 255), 2)

            line_points = [start_pt, end_pt]
            # print(line_points)
            if start_pt in all_start_point_list:
                pass
            else:
                uniq_line_start_end_points.append(line_points)
                # add new circle all points
                all_start_point_list = all_start_point_list + support_class.points_in_circle_np(25, start_pt[0],
                                                                                                start_pt[1])
                # Example usage: () rangel
                x1, y1 = start_pt[0], start_pt[1]  # Top-left corner
                x2, y2 = end_pt[0], end_pt[1] + 60  # Bottom-right corner

                # print(x1)
                # print(y1)
                # print(x2)
                # print(y2)

                integer_points = support_class.get_integer_points_in_rectangle(x1, y1, x2, y2)
                all_start_point_list = all_start_point_list + integer_points
                # print(integer_points)

                # print(line_points)
                cv2.line(img, start_pt, end_pt, (0, 0, 255), 10)
                cv2.putText(img, 'point {:d}, {:d}, {}'.format(line_points[0][0], line_points[0][1], x), line_points[0],
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                # print(all_start_point_list)
                x = x + 1

    # print(len(uniq_line_start_end_points))

    line_count = len(uniq_line_start_end_points)
    print(image_path)
    if line_count != 15:
        print(line_count)
    cv2.putText(img, '{}'.format(line_count), (500, 500),
                cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 0, 0), 2, cv2.LINE_AA)

    # TODO uncomment for testing
    # cv2.imwrite('img/line_detect_final/' + save_file_name, img)
    # cv2.imwrite(save_file_name, img)
    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return uniq_line_start_end_points

# line_detect_points('img/line_added_sample/page-177.png')
# line_detect_points('sample.png')
