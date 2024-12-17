from page import SbisPage


def test_sbis_contacts_page(browser):
    sbis_page = SbisPage(browser)
    sbis_page.go_to_site()
    contacts_page = sbis_page.click_contacts()

    region_title = contacts_page.get_region()
    assert "Самарская обл." in region_title, f"Unexpected region title: {region_title}"
    # region_partners = contacts_page.get_region_partners()
    # assert region_partners.is_displayed(), "Block is not visible"
    assert "СБИС - Самара" in contacts_page.get_region_partner_name()

    contacts_page.click_region_chooser()
    contacts_page.choose_41_region()
    new_region_title = contacts_page.get_region()
    assert "Камчатский край" in new_region_title, f"Unexpected region title: {new_region_title}"
    assert "СБИС Контакты — Камчатский край" in contacts_page.get_page_title()
    assert "https://sbis.ru/contacts/41-kamchatskij-kraj" in contacts_page.get_page_url()
    assert "СБИС - Камчатка" in contacts_page.get_region_partner_name()
