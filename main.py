import detect_ayah
import support_class

########################################################################################################################
# TODO ayah detect
save_file_names = []  # all image names
all_file_names = support_class.get_file_names("img/surah_border_less_sample/", "")
image_count = len(all_file_names)
print(image_count)

next_page_start = 1
for i in range(0, image_count):
    save_file_name = 'page-{0:03}.png'.format(i + 1)
    image_path = 'img/surah_border_less_sample/' + save_file_name
    uniq_detected_points, end_index = (
        detect_ayah.page_ayah_detect(image_path, next_page_start, save_file_name))
    next_page_start = end_index

print(next_page_start)
########################################################################################################################
