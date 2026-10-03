from pages.home_page import HomePage
from pages.english_page import EnglishPage


def test_todo_english(page):
    home_page = HomePage(page)
    english_page = EnglishPage(page)

    # 홈페이지 접속
    home_page.open()

    # 대한민국/한국어 선택
    #home_page.select_korea()

    # 토도영어 이동
    home_page.click_todo_english()
    page.wait_for_url("**/kr/english")

    # URL 확인
    assert "/kr/english" in page.url

    # 영어 페이지 제목 확인
    assert english_page.is_element_visible(
        english_page.english_title
    )

    # 무료체험 버튼 노출 확인
    assert english_page.is_element_visible(
        english_page.free_trial_button
    )

    # 고객센터 Floating 버튼 노출 확인
    assert english_page.is_element_visible(
        english_page.floating_cs_button
    )

    # Floating 무료체험 버튼 확인을 위해 하단으로 스크롤
    english_page.scroll_to_element(
        english_page.floating_cs_button
    )

    assert english_page.is_element_visible(
        english_page.float_free_trial_button
    )

    # 커리큘럼 자세히보기 버튼 확인
    english_page.scroll_to_element(
        english_page.curriculum_button
    )

    assert english_page.is_element_visible(
        english_page.curriculum_button
    )

    # 소셜 인터뷰 더보기 버튼 확인
    english_page.scroll_to_element(
        english_page.social_interview_button
    )

    assert english_page.is_element_visible(
        english_page.social_interview_button
    )

    # 토도영어 앱 다운받기 버튼 확인
    english_page.scroll_to_element(
        english_page.download_app_button
    )

    assert english_page.is_element_visible(
        english_page.download_app_button
    )

    # 멤버십 구매하기 버튼 확인
    english_page.scroll_to_element(
        english_page.membership_button
    )

    assert english_page.is_element_visible(
        english_page.membership_button
    )

    # SNS 링크 영역 확인
    english_page.scroll_to_element(
        english_page.sns_links.first
    )

    assert english_page.sns_links.count() == 4

    for index in range(4):
        assert english_page.sns_links.nth(index).get_attribute("href")

    # region 영역 확인
    english_page.scroll_to_element(
        english_page.korea_region.first
    )

    assert english_page.korea_region.is_visible()

    # region 영역 확인
    english_page.scroll_to_element(
        english_page.footer_company_links.first
    )

    assert english_page.privacy_policy_link.get_attribute("href") == "/kr/docs/pp"
    assert english_page.terms_link.get_attribute("href") == "/kr/docs/tos"
    assert english_page.legal_notice_link.get_attribute("href") == "/kr/docs/legal"

    # copyright영역 확인
    english_page.scroll_to_element(
        english_page.enuma_copyright_link
    )

    assert english_page.is_element_visible(
        english_page.enuma_copyright_link
    )

    assert english_page.enuma_copyright_link.get_attribute(
        "href"
    ) == "https://enuma.com/ko"

    assert english_page.enuma_copyright_link.get_attribute(
        "target"
    ) == "_blank"
