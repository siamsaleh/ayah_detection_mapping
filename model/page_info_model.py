class PageInfo:

    def __init__(self, page_no, surah_no, start_ayah_no):
        self.page_no = page_no
        self.surah_no = surah_no
        self.start_ayah_no = start_ayah_no

    def print_values(self):
        print(f'page {self.page_no} index {self.surah_no} line {self.start_ayah_no}')
