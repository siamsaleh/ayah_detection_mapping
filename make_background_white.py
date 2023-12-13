import support_class
import os

save_file_names = []  # all image names
all_file_names = support_class.get_file_names("sample/", "")
image_count = len(all_file_names)
print(image_count)

count = 1
index = 0
for i in range(0, image_count):
    save_file_name = 'page-{0:03}.png'.format(i + 1)
    image_path = 'sample/' + save_file_name

    string = 'python3 utils/make_white.py "sample/' + save_file_name + '" '
    string = string + '"white_sample/' + save_file_name + '"'
    os.system(string)
    count = count + 1
    index = index + 1
    print(string + ' index - {:03d}\n'.format(index))


# img = cv2.imread('sample/page-600.png', 0)
# h, w = img.shape
# cv2.line(img, (0, 0), (w, 0), (255, 255, 255), 30)
# cv2.imshow("LSD", img)
# cv2.waitKey(0)

# img = cv2.imread(image_path, 0)
# h, w = img.shape
# cv2.line(img, (0, 0), (w, 0), (0, 0, 255), 25)

