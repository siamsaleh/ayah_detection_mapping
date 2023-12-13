from PIL import Image, ImageOps
import cv2
import support_class

all_file_names = support_class.get_file_names("white_sample/", "")
image_count = len(all_file_names)
print(image_count)

for i in range(0, image_count):
    save_file_name = 'page-{0:03}.png'.format(i + 1)
    image_path = 'white_sample/' + save_file_name

    img = cv2.imread(image_path, 0)
    h, w = img.shape

    cv2.line(img, (0, 0), (w, 0), (255, 255, 255), 30)
    cv2.line(img, (0, 0), (0, h), (255, 255, 255), 30)
    cv2.line(img, (w, 0), (w, h), (255, 255, 255), 30)
    cv2.line(img, (0, h), (w, h), (255, 255, 255), 30)

    cv2.imwrite('borderless_sample/' + save_file_name, img)
    print('index - {:03d}\n'.format(i))
