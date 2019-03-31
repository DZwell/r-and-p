import re
import time
from selenium.webdriver.common.keys import Keys


def calculate_sales(browser, bsr_cat):
    '''Returns sales estimate'''

    print('Calculating sales...\n')

    browser.execute_script("window.open('https://www.junglescout.com/estimator/', 'new_window')")
    time.sleep(2)
    browser.switch_to_window(browser.window_handles[1])

    # BSR looks like "#54, 123". Need to strip out special chars
    normalized_bsr = re.sub('[#,]', '', bsr_cat[0])
    # Fill in BSR
    time.sleep(1)
    browser.find_elements_by_xpath('//td/input')[0].send_keys(normalized_bsr)

    # Select marketplace
    browser.find_elements_by_xpath('//i[@class="x-icon x-icon-caret-down"]')[0].click()
    time.sleep(1)
    browser.find_elements_by_xpath('//span[text()="United States of America"]')[0].click()

    # Select category
    browser.find_elements_by_xpath('//i[@class="x-icon x-icon-caret-down"]')[1].click()
    category_xpath = '//span[text()="{}"]'.format(bsr_cat[1])
    time.sleep(1)
    browser.find_elements_by_xpath(category_xpath)[0].click()
    time.sleep(1)
    # Submit
    browser.find_elements_by_xpath('//a[@class="js-est-btn"]')[0].click()
    time.sleep(1)

    monthly_sales = browser.find_elements_by_xpath('//p[@class="js-magic-result"]')[0].text

    return monthly_sales

    
