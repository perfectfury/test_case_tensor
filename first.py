from page import SbisPage


def test_sbis_page(browser):
    sbis_page = SbisPage(browser)
    sbis_page.go_to_site()
    contacts_page = sbis_page.click_contacts()
    tensor_page = contacts_page.click_banner()

    card = tensor_page.get_card()
    assert card.is_displayed(), "Card is not visible"
    card_title = tensor_page.get_card_title(card)
    assert "Сила в людях" in card_title, f"Unexpected card title: {card_title}"
    tensor_about_page = tensor_page.navigate_to_about(card)

    block = tensor_about_page.get_block()
    assert block.is_displayed(), "Block is not visible"
    block_title = tensor_about_page.get_block_title(block)
    assert "Работаем" in block_title, f"Unexpected block title: {block_title}"

    images = tensor_about_page.get_block_images(block)
    assert images, "No images found in the block"
    assert all(img.size == images[0].size for img in images), "Images are not equal in size"
