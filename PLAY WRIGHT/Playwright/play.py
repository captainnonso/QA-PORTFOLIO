from playwright.sync_api import sync_playwright
from objects import List

def unit():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        obj =  List(page)
        obj.navigate()
        obj.login()
        obj.password()
        obj.thesi()
        browser.close()

if __name__ == "__main__":
  unit()

def test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        obj =  List(page)
        obj.navigate()
        obj.login()
        obj.password()
        obj.thesi()
        browser.close()

if __name__ == "__main__":
  test()


  def lust():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        obj =  List(page)
        obj.navigate()
        obj.login()
        obj.password()
        obj.thesi()
        browser.close()

if __name__ == "__main__":
  lust()
