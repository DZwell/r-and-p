import re
from selenium.webdriver.common.keys import Keys


def calculate_sales(browser, bsr_cat):
    '''Returns sales estimate'''

    browser.execute_script("window.open('https://www.junglescout.com/estimator/', 'new_window')")

    import pdb; pdb.set_trace()
    # BSR looks like "#54, 123". Need to strip out special chars
    normalized_bsr = re.sub('[#,]', '', bsr_cat[0])
    bsr_field = str("javascript:document.getElementsByName('theRankInput')[0].value = {}").format(normalized_bsr)
    browser.execute_script(bsr_field)
    # browser.send_keys(bsr_cat[0])
    # marketplace = browser.find_element_by_xpath('//span[text()="United States of America"]')
    # product_category = browser.find_element_by_xpath('//span[@title={}]').format(bsr_cat[1])

    print('Calculating sales...\n')
    
