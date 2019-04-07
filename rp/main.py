import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sheet import get_item_codes, write_to_sheet
from jungle import clear_search_field, search_asin
from scout import calculate_sales

start_time = time.time()
monthly_sales_list = []
log_file = open('log.txt', 'w')

print('\nInitializing...\n')

item_codes = get_item_codes(os.environ['SHEET_ID'])
total_item_code_count = len(item_codes)
count = 1

chrome_options = Options()
# chrome_options.add_argument("--headless") 
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.amazon.com/ref=nav_logo')

for i in item_codes:
    print('Item {}/{}\n'.format(count, total_item_code_count))
    bsr_cat = search_asin(browser, i, log_file)
    monthly_sales = calculate_sales(browser, bsr_cat)
    monthly_sales_list.append([monthly_sales])
    browser.switch_to_window(browser.window_handles[0])
    clear_search_field(browser)
    count += 1

write_to_sheet(monthly_sales_list, os.environ['SHEET_ID'])
elapsed_time = time.time() - start_time
pretty_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
print('Done!\n')
print('Elapsed time: {}'.format(pretty_time))
log_file.close()
