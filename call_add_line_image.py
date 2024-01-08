import line_detect
import support_class

# this class create images of all line_detect (uncomment in line_detect)
########################################################################################################################
# TODO line detect
save_file_names = []  # all image names
all_file_names = support_class.get_file_names("img/line_test/", "")
image_count = len(all_file_names)
print(image_count)

for i in range(0, image_count):
    save_file_name = 'page-{0:03}.png'.format(i + 1)
    image_path = 'img/line_test/' + save_file_name
    uniq_line_start_end_points = line_detect.line_detect_points(image_path, save_file_name)
########################################################################################################################
