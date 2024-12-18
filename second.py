from page import SbisPage


def test_sbis_contacts_page(browser):
    sbis_page = SbisPage(browser)
    sbis_page.go_to_site()
    contacts_page = sbis_page.click_contacts()

    expected_region_title = "Оренбургская обл."
    expected_region_partner = "СБИС - Оренбург"
    actual_region_title = contacts_page.get_region()
    assert contacts_page.check_region(expected_region_title), f"Expected: {expected_region_title}, found: {actual_region_title}"
    assert expected_region_partner in contacts_page.get_region_partner_name()

    expected_41region_title = "Камчатский край"
    expected_41region_page_title = "СБИС Контакты — Камчатский край"
    expected_41region_page_url = "https://sbis.ru/contacts/41-kamchatskij-kraj"
    expected_41region_partner = "СБИС - Камчатка"
    contacts_page.click_region_chooser()
    contacts_page.choose_41_region()
    new_region_title = contacts_page.get_region()
    assert contacts_page.check_region(expected_41region_title), f"Expected: {expected_41region_title}, found: {new_region_title}"
    assert expected_41region_page_title in contacts_page.get_page_title()
    assert expected_41region_page_url in contacts_page.get_page_url()
    assert expected_41region_partner in contacts_page.get_region_partner_name()
