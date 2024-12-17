from selenium.webdriver.common.by import By


class SbisPageLocators(object):
    CONTACTS = (By.LINK_TEXT, 'Контакты')


class SbisContactsPageLocators(object):
    BANNER = (By.XPATH, "//div[@id='contacts_clients']//a[@href='https://tensor.ru/']")
    REGION = (By.CLASS_NAME, "sbis_ru-Region-Chooser__text")
    REGION_41 = (By.XPATH, "//span[@title='Камчатский край']")
    PARTNER = (By.CSS_SELECTOR, "div.sbisru-Contacts-List__name")



class TensorPageLocators(object):
    CARD_CONTAINER = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-content.tensor_ru-Index__card")
    CARD_TITLE = (By.CSS_SELECTOR, "p.tensor_ru-Index__card-title")
    CARD_ABOUT = (By.CSS_SELECTOR, "a.tensor_ru-link.tensor_ru-Index__link")


class TensorAboutPageLocators(object):
    BLOCK_CONTAINER = (By.CSS_SELECTOR, "div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3")
    BLOCK_TITLE = (By.CSS_SELECTOR, "h2.tensor_ru-header-h2.tensor_ru-About__block-title")
    BLOCK_GRID = (By.CLASS_NAME, "s-Grid-container")
    BLOCK_IMAGES = (By.TAG_NAME, "img")
