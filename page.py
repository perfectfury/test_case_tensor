import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import *

logger = logging.getLogger(__name__)
filehandler = logging.FileHandler('logfile.log')
formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)
logger.setLevel(logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://sbis.ru/"

    def find_element(self, locator, time=10):
        logger.info(f"Finding element by locator: {locator}")
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        logger.info(f"Finding elements by locator: {locator}")
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        logger.info(f"Navigating to site: {self.base_url}")
        return self.driver.get(self.base_url)

    def go_to_new_tab(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[-1])
        except IndexError:
            raise Exception("No new tab found to switch to")

    def get_page_title(self):
        logger.info(f"Getting the page title: {self.driver.title}")
        return self.driver.title

    def get_page_url(self):
        logger.info(f"Getting the page URL: {self.driver.current_url}")
        return self.driver.current_url


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

    def get_region(self):
        logger.info("Getting the region title")
        region_title = self.find_element(SbisContactsPageLocators.REGION).text
        logger.info(f"Got the region title: {region_title}")
        return region_title

    def check_region(self, value):
        logger.info(f"Comparing region title with expected: {value}")
        try:
            return WebDriverWait(self.driver, 3).until(
                EC.text_to_be_present_in_element(SbisContactsPageLocators.REGION, value))
        except TimeoutException:
            return False

    def click_region_chooser(self):
        logger.info("Clicking on the region chooser")
        self.find_element(SbisContactsPageLocators.REGION).click()

    def choose_41_region(self):
        logger.info("Choosing region 41")
        try:
            return WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(SbisContactsPageLocators.REGION_41)).click()
        except TimeoutException:
            return False

    def get_region_partner_name(self):
        logger.info("Getting the region partner")
        name = self.find_element(SbisContactsPageLocators.PARTNER).text
        logger.info(f"Got the region partner: {name}")
        return name


class TensorPage(BasePage):
    def get_card(self):
        logger.info("Getting the card on the tensor.ru")
        return self.find_element(TensorPageLocators.CARD_CONTAINER)

    def get_card_title(self, element):
        logger.info("Getting the card title")
        return element.find_element(*TensorPageLocators.CARD_TITLE).text

    def navigate_to_about(self, element):
        logger.info("Navigating to the tensor.ru/about")
        about_link = element.find_element(*TensorPageLocators.CARD_ABOUT)
        logger.info(f"About page URL: {about_link.get_attribute('href')}")
        about_link.click()
        return TensorAboutPage(self.driver)


class TensorAboutPage(BasePage):
    def get_block(self):
        logger.info("Checking the block on the tensor.ru/about")
        return self.find_element(TensorAboutPageLocators.BLOCK_CONTAINER)

    def get_block_title(self, element):
        logger.info("Getting the block title")
        return element.find_element(*TensorAboutPageLocators.BLOCK_TITLE).text

    def get_block_images(self, element):
        logger.info("Checking image sizes in the block")
        grid = element.find_element(*TensorAboutPageLocators.BLOCK_GRID)
        return grid.find_elements(*TensorAboutPageLocators.BLOCK_IMAGES)
