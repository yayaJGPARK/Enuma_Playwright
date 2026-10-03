# pages/english_page.py

from playwright.sync_api import Page


class EnglishPage:

    def __init__(self, page: Page):
        self.page = page

        self.english_title = page.get_by_role(
            "heading",
            name="효과로 말하는 1등 영어! 토도영어"
        )

        self.free_trial_button = page.locator(
            "#features"
        ).get_by_text(
            "회원가입하고 7일간 무료체험하기",
            exact=True
        )

        self.float_free_trial_button = page.locator(
            ".float-btn",
            has_text="회원가입하고 7일간 무료체험하기"
        )

        self.floating_cs_button = page.locator(
            "img.img_cs_channelio"
        )

        self.curriculum_button = page.get_by_text(
            "커리큘럼 자세히보기",
            exact=True
        )

        self.social_interview_button = page.get_by_text(
            "소셜 인터뷰 더보기",
            exact=True
        )

        self.download_app_button = page.get_by_text(
            "토도영어 앱 다운받기",
            exact=True
        )

        self.membership_button = page.locator(
            ".benefit_plan_membership"
        )

        self.sns_links = page.locator(
            ".sns li a"
        )

        self.korea_region = page.locator(
            "ul.region li"
        ).filter(
            has_text="대한민국"
        )

        self.footer_company_links = page.locator(
            ".footer-company li a"
        )

        self.privacy_policy_link = page.get_by_text(
            "개인정보처리방침",
            exact=True
        )

        self.terms_link = page.get_by_text(
            "이용약관",
            exact=True
        )

        self.legal_notice_link = page.get_by_text(
            "법적고지",
            exact=True
        )

        self.enuma_copyright_link = page.locator(
            ".copyright_enuma a"
        )

    def scroll_to_element(self, locator):
        locator.scroll_into_view_if_needed()

    def is_element_visible(self, locator):
        locator.wait_for(state="visible")
        return locator.is_visible()