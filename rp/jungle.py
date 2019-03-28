from categories import categories


def search_asin(browser, item_code):
    '''Search for asin'''

    search_field = browser.find_element_by_id('twotabsearchtextbox')
    click_search_button = str("javascript:document.getElementById('nav-search-submit-text').nextElementSibling.click()")

    click_found_item_link = str("javascript:document.getElementsByClassName('s-image')[0].click()")
    search_field.send_keys(item_code)
    browser.execute_script(click_search_button)
    browser.execute_script(click_found_item_link)

    return get_bsr_and_category(browser)


def get_bsr_and_category(browser):
    '''Returns a tuple (best seller rank, category)'''

    try:
        li = browser.find_element_by_id('SalesRank')
    except Exception:
        li = None

    try:
        span_list = browser.find_elements_by_xpath("//span[contains(text(),'#')]")
    except Exception:
        span_list = None

    if li:
        category = get_category(li.text)
        li_text_list = li.text.split(' ')
        bsr = [string for string in li_text_list if '#' in string][0]
        return (bsr, category)
    elif span_list:
        category = get_category(span_list[0].text)
        bsr = span_list[0].text.split(' ')[0]
        return (bsr, category)


def get_category(bsr_text_string):
    '''Return itme category'''
    return [c for c in categories if c in bsr_text_string].pop()


def clear_search_field(browser):
    '''Clear search field'''
    
    search_field = browser.find_element_by_id('twotabsearchtextbox')
    search_field.clear()    

