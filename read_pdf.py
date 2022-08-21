import re

from PyPDF2 import PdfReader

reader = PdfReader("Lai-T6.pdf")
number_of_pages = len(reader.pages)
for i in range(number_of_pages):
    try:
        page = reader.pages[i]
        data = page.extract_text()
        regex_order_no = re.compile(r"Tổng số tiền phải trả: (\S+)")
        order_no = re.search(regex_order_no, data).group(1)
        print(order_no)
    except:
        pass