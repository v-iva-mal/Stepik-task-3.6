import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_search_Add_to_basked_button(browser):
    browser.get(link)
   # time.sleep(30)
    Add_to_cart = len(browser.find_elements_by_css_selector("button.btn-add-to-basket"))
    assert Add_to_cart > 0, f"No seach button  'Add to basked'"

