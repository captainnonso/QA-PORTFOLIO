class List:

  def __init__(self, page):
    self.page = page

  def navigate(self):
    self.page.goto("https://dev-payment-pro.blusalt.net/")

  def login(self):
   self.page.fill("#email", "abass@blusalt.net")

  def password(self):
     self.page.fill("#password", "@Blusalt2026")

  def thesi(sub):
     sub.page.click("//button[@type='submit']")
     sub.page.screenshot(path = "test.png")
     print(sub.page.title())


     