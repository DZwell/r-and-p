
def search_asin(browser, item_code):
    browser.get('https://www.amazon.com/ref=nav_logo')

    search_field = browser.find_element_by_id('twotabsearchtextbox')
    click_search_button = str("javascript:document.getElementById('nav-search-submit-text').nextElementSibling.click()")
    click_found_item_link = str("javascript:document.getElementsByClassName('a-size-medium s-inline  s-access-title  a-text-normal')[0].click()")

    search_field.send_keys(item_code)
    browser.execute_script(click_search_button)
    browser.execute_script(click_found_item_link)
    x = browser.find_elements_by_xpath("//td/span/span/a")
    import pdb; pdb.set_trace()

