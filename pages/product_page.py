from playwright.sync_api import Page


class ProductPage:

    def __init__(self, page: Page):
        self.page = page

        self.math_banner = page.locator(
            'img.visible-desktop[alt="공간 감각부터 논리 추리까지? 사고력 세상으로 모험을 떠나 보세요"]'
        )

        self.hangeul_banner = page.locator(
            'img.visible-desktop[alt="학습목표 중심의 미션모드. 연습이 필요한 부분만 골라 반복 학습!"]'
        )

        self.english_title = page.get_by_role(
            "heading",
            name="효과로 말하는 1등 영어! 토도영어"
        )

    def is_element_visible(self, locator):
        locator.wait_for(state="visible")
        return locator.is_visible()