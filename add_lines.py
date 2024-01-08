import cv2


def page_add_lines(image_path, save_file_name):

    img = cv2.imread(image_path)
    print(image_path)

    start_x = 965
    end_x = 50
    y = 143
    for x in range(1, 16):
        cv2.line(img, (start_x, y), (end_x, y), (0, 0, 0), 2)
        y = y + 90
        if x / 5:
            y = y + 5

    cv2.imwrite("img/line_added_sample/" + save_file_name, img)

    # cv2.imshow("img", img)
    # cv2.waitKey(0)


# page_add_lines("sample/page-005.png", "res.png")
