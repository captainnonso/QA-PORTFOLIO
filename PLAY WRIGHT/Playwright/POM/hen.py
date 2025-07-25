from playwright.sync_api import sync_playwright
from PageObject.logs import SearchPage

def lest():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Now pass the page to SearchPage
        search_page = SearchPage(page)
        search_page.navigate()
        search_page.search()
        search_page.payment()

        page.wait_for_timeout(3000)
        browser.close()

if __name__ == "__main__":
    lest()
