import add_lines
import support_class

# this class create lines in all images
########################################################################################################################
# TODO add line
save_file_names = []  # all image names
all_file_names = support_class.get_file_names("img/surah_border_less_sample/", "")
image_count = len(all_file_names)
print(image_count)

for i in range(0, image_count):
    save_file_name = 'page-{0:03}.png'.format(i + 1)
    image_path = 'img/surah_border_less_sample/' + save_file_name
    add_lines.page_add_lines(image_path, save_file_name)

########################################################################################################################
