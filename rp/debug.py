import os
from main import browser


def catpure_errors(e, item_code):
    if not os.path.isdir('captures'):
        os.mkdir(f'{item_code}')
    log_error(e, item_code)

def log_error(e, item_code):
    log_file = open('errors.log', 'w')
    log_file.write('Problem with item {}\n{}\n'.format(item_code, e))

def take_screenshot(item_code):
    browser.get_screenshot_as_file(f'{item_code}.png')

