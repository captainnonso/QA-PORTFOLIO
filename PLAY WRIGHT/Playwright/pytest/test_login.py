from playwright.sync_api import sync_playwright
from PageObject.logs import Loginpage


with sync_playwright() as p:
      
     def test_login(page):
      browser = p.chromium.launch()
      Login_page = Loginpage(page)
      Login_page.navigate()
      Login_page.search('iii')
      
