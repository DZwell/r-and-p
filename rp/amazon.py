
def search_asin(browser, item_code):
    '''Search for asin'''

    search_field = browser.find_element_by_id('twotabsearchtextbox')
    click_search_button = str("javascript:document.getElementById('nav-search-submit-text').nextElementSibling.click()")
    click_found_item_link = str("javascript:document.getElementsByClassName('a-size-medium s-inline  s-access-title  a-text-normal')[0].click()")

    search_field.send_keys(item_code)
    browser.execute_script(click_search_button)
    browser.execute_script(click_found_item_link)

    bsr = get_bsr(browser)
    print('Item code: {}\nBest seller rank: {}'.format(item_code, bsr))


def get_bsr(browser):
    '''Return best seller rank'''

    try:
        li = browser.find_element_by_id('SalesRank')
    except Exception:
        li = None

    try:
        span_list = browser.find_elements_by_xpath("//span[contains(text(),'#')]")
    except Exception:
        span_list = None

    if li:
        li_text_list = li.text.split(' ')
        return [string for string in li_text_list if '#' in string][0]
    elif span_list:
        return span_list[0].text.split(' ')[0]


def clear_search_field(browser):
    '''Clear search field'''
    search_field = browser.find_element_by_id('twotabsearchtextbox')
    search_field.clear()    

