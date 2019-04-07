from categories import categories


def search_asin(browser, item_code, log_file):
    '''Search for asin'''

    print('Searching...\n')
    search_field = browser.find_element_by_id('twotabsearchtextbox')
    click_search_button = str("javascript:document.getElementById('nav-search-submit-text').nextElementSibling.click()")

    click_found_item_link = str("javascript:document.getElementsByClassName('s-image')[0].click()")
    search_field.send_keys(item_code)
    browser.execute_script(click_search_button)
    browser.execute_script(click_found_item_link)

    try:
        return get_bsr_and_category(browser)
    except Exception as e:
        log_file.write('Problem with item {}\n{}\n'.format(item_code, e))


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
    elif span_list:
        category = get_category(span_list[0].text)
        bsr = span_list[0].text.split(' ')[0]
    
    scrubbed_category = scrub_category(category)
    return (bsr, scrubbed_category)


def get_category(bsr_text_string):
    '''Return item category'''
    return [c for c in categories if c in bsr_text_string].pop()


def clear_search_field(browser):
    '''Clear search field'''
    
    search_field = browser.find_element_by_id('twotabsearchtextbox')
    search_field.clear() 

def scrub_category(cat):
    if cat 

