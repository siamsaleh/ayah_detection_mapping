import detect_ayah
import support_class

#####################################
# page info
from model.page_info_model import PageInfo
import pandas as pd
import support_class
import index_to_data

# CSV
dataFrame = pd.DataFrame(columns=['page_no', 'surah_no', 'start_ayah_no'])


def save_csv(pg_info, data_frame):
    new_row = pd.DataFrame(
        {'page_no': [pg_info.page_no], 'surah_no': [pg_info.surah_no], 'start_ayah_no': [pg_info.start_ayah_no]})
    return pd.concat([data_frame, new_row], ignore_index=True)


#####################################

# this class create images of all ayah_detect (uncomment in ayah_detect)
########################################################################################################################
# TODO ayah detect
save_file_names = []  # all image names
all_file_names = support_class.get_file_names("img/surah_border_less_sample/", "")
image_count = len(all_file_names)
print(image_count)

next_page_start = 13
for i in range(0, image_count):
    save_file_name = 'page-{0:03}.png'.format(i + 1)
    image_path = 'img/surah_border_less_sample/' + save_file_name
    uniq_detected_points, end_index = (
        detect_ayah.page_ayah_detect(image_path, next_page_start, save_file_name))
    next_page_start = end_index

print(next_page_start)
########################################################################################################################
# TODO page info detect
# index = 1
# position = 1
# start_page = 1
# end_page = 605
# for page in range(start_page, end_page + 1):
#     print(page)
#     save_file_name = 'page-{0:03}.png'.format(page)
#     image_path = 'img/surah_border_less_sample/' + save_file_name
#
#     surah_no, start_ayah_number = index_to_data.get_surah_ayah_no(index)
#     page_info = PageInfo(page, surah_no, start_ayah_number)
#     dataFrame = save_csv(page_info, dataFrame)
#
#     end_index = detect_ayah.page_info_method(image_path, index, "test.png")
#     index = end_index
#
# # save CSV file
# dataFrame.to_csv("page_info.csv", index=True)
