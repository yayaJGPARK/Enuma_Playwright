# pages/english_page.py

from playwright.sync_api import Page


class EnglishPage:

    def __init__(self, page: Page):
        self.page = page

        self.english_title = page.get_by_role(
            "heading",
            name="효과로 말하는 1등 영어! 토도영어"
        )

    def is_element_visible(self, locator):
        locator.wait_for(state="visible")
        return locator.is_visible()