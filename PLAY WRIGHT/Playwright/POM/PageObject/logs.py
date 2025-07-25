# PageObject/logs.py

class SearchPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://dev-payment-pro.blusalt.net/")

    def search(self):
        search_box = self.page.locator("#email")
        search_box.fill("abass@blusalt.net")
        self.page.fill("#password",'@Blusalt2026')
        self.page.keyboard.press("Enter")
        print(self.page.title())
   
    def payment(self):
       self.page.click("//a[@href='/payment-gateway/transactions']//span")
       
       self.page.click("a[id='radix-:r1p:-trigger-Refunds']")
    
