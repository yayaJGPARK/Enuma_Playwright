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


