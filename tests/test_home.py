from pages.home_page import HomePage
from pages.product_page import ProductPage

def test_home(page):
    home_page = HomePage(page)
    product_page = ProductPage(page)

    home_page.open()
   # assert page.get_by_text("국가 또는 지역을 선택해주세요").is_visible()

    #home_page.select_korea()

    # 토도수학
    home_page.click_todo_math()
    page.wait_for_url("**/kr/math")
    assert "/kr/math" in page.url
    assert product_page.is_element_visible(product_page.math_banner)

    # 토도한글
    home_page.click_todo_hangeul()
    page.wait_for_url("**/kr/hangeul")
    assert "/kr/hangeul" in page.url
    assert product_page.is_element_visible(product_page.hangeul_banner)

    # 토도영어
    home_page.click_todo_english()
    page.wait_for_url("**/kr/english")
    assert "/kr/english" in page.url
    assert product_page.is_element_visible(product_page.english_title)