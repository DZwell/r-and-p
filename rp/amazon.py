import os
import sys
import time
from sheet import get_item_codes, write_to_sheet
# from creds_file import get_creds, set_creds
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
start_time = time.time()

print('\nInitializing...\n')

# if not os.path.isfile('creds.json'):
#     creds_file = open('creds.json', 'w')
#     set_creds(creds_file)

# creds = get_creds(open('creds.json', 'r'))

item_codes = get_item_codes(os.environ['SHEET_ID'])
item_status_list = []
not_available = 'N/A'
count = 1


# Selenium setup
if getattr(sys, 'frozen', False):
    # running in a bundle
    base_dir = sys._MEIPASS
else:
    # running normally
    base_dir = os.path.dirname(os.path.abspath(__file__))

# chrome_path = os.path.join(base_dir, 'selenium', 'webdriver', 'chromedriver.exe')
chrome_options = Options()
# chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.amazon.com/ref=nav_logo')

print('Searching...\n')

search_field = browser.find_element_by_id('twotabsearchtextbox')
click_search_button = str("javascript:document.getElementById('nav-search-submit-text').nextElementSibling.click()")

for i in item_codes:
    search_field.send_keys(i)
    browser.execute_script(click_search_button)

elapsed_time = time.time() - start_time
pretty_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
print('Done!\n')
print('Elapsed time: {}'.format(pretty_time))