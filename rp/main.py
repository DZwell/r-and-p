import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sheet import get_item_codes, write_to_sheet
from jungle import clear_search_field, search_asin
from scout import calculate_sales

start_time = time.time()

print('\nInitializing...\n')

item_codes = get_item_codes(os.environ['SHEET_ID'])
count = 1

chrome_options = Options()
# chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.amazon.com/ref=nav_logo')

print('Searching...\n')

for i in item_codes:
    bsr_cat = search_asin(browser, i)
    calculate_sales(browser, bsr_cat)
    clear_search_field(browser)

elapsed_time = time.time() - start_time
pretty_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
print('Done!\n')
print('Elapsed time: {}'.format(pretty_time))