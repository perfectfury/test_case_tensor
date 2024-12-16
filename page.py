import logging

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://sbis.ru/"

    def find_element(self, locator, time=10):
        logger.info(f"Finding element by locator: {locator}")
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        logger.info(f"Finding elements by locator: {locator}")
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        logger.info(f"Navigating to site: {self.base_url}")
        return self.driver.get(self.base_url)

    def go_to_new_tab(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[-1])
        except IndexError:
            raise Exception("No new tab found to switch to")


class SbisPage(BasePage):
    def click_contacts(self):
        logger.info("Clicking on the Contacts link")
        self.find_element(SbisPageLocators.CONTACTS, time=5).click()
        return SbisContactsPage(self.driver)


class SbisContactsPage(BasePage):
    def click_banner(self):
        logger.info("Clicking on the banner")
        self.find_element(SbisContactsPageLocators.BANNER, time=5).click()
        self.go_to_new_tab()
        return TensorPage(self.driver)


class TensorPage(BasePage):
    def get_card(self):
        logger.info("Getting the card on the tensor.ru")
        return self.find_element(TensorPageLocators.CARD_CONTAINER)

    def get_card_title(self, card):
        logger.info("Getting the card title")
        return card.find_element(*TensorPageLocators.CARD_TITLE).text

    def navigate_to_about(self, card):
        logger.info("Navigating to the tensor.ru/about")
        about_link = card.find_element(*TensorPageLocators.CARD_ABOUT)
        logger.info(f"About page URL: {about_link.get_attribute('href')}")
        about_link.click()
        return TensorAboutPage(self.driver)


class TensorAboutPage(BasePage):
    def get_block(self):
        logger.info("Checking the block on the tensor.ru/about")
        return self.find_element(TensorAboutPageLocators.BLOCK_CONTAINER)

    def get_block_title(self, block):
        logger.info("Getting the block title")
        return block.find_element(*TensorAboutPageLocators.BLOCK_TITLE).text

    def get_block_images(self, block):
        logger.info("Checking image sizes in the block")
        grid = block.find_element(*TensorAboutPageLocators.BLOCK_GRID)
        return grid.find_elements(*TensorAboutPageLocators.BLOCK_IMAGES)
