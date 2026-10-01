from playwright.sync_api import Page


class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.korea_radio = page.get_by_text("대한민국/한국어")
        self.todo_math = page.locator('a[href="/kr/math"]')
        self.todo_hangeul = page.locator('a[href="/kr/hangeul"]')
        self.todo_english = page.locator('a[href="/kr/english"]')

    def open(self):
        self.page.goto("https://todoschool.com/")

    def select_korea(self):
        self.korea_radio.click()

    def click_todo_math(self):
        self.todo_math.click()

    def click_todo_hangeul(self):
        self.todo_hangeul.click()

    def click_todo_english(self):
        self.todo_english.click()