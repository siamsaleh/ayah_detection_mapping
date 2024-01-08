import support_class
import os

all_file_names = support_class.get_file_names("sample/", "")
all_file_names = sorted(all_file_names)
image_count = len(all_file_names)
print(image_count)

for i in range(0, image_count):
    save_file_name = 'page-{0:03}.png'.format(i + 1)
    image_path = 'sample/' + all_file_names[i]

    string = 'python3 utils/make_white.py "' + image_path + '" '
    string = string + '"white_sample/' + save_file_name + '"'
    os.system(string)
    print(string + ' index - {:03d}\n'.format(i + 1))
