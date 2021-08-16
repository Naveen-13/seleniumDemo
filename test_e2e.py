
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.checkoutPage import checkoutPage
from PageObjects.homePage import homePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homepage = homePage(self.driver)
        checkoutpage = homepage.getShopItem()
        log.info("Getting card titles")
        # checkoutpage = checkoutPage(self.driver)
        # checkoutpage.getCheckoutItems()
        # self.driver.find_element_by_link_text("Shop").click()
        allProducts = checkoutpage.getCheckoutItems()
        # self.driver.find_elements_by_xpath("//div[@class='card h-100']")

        # xpath for selecting text of phone names "//div[@class='card h-100']/div/h4/a"

        for productName in allProducts:
            # name = productName.find_element_by_xpath("div/h4/a").text
            name = checkoutpage.getElementName
            if name == "Blackberry":
                # xpath for add cart button $x("//div[@class='card h-100']/div/button")
                productName.find_element_by_xpath("div/button").click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        self.driver.find_element_by_css_selector(".btn-success").click()
        log.info("Entering country name ind")
        self.driver.find_element_by_css_selector("#country").send_keys("ind")

        # wait = WebDriverWait(self.driver, 7)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.linkPresenceWait("India")

        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_class_name("btn-success").click()
        successText = self.driver.find_element_by_class_name("alert-success").text
        log.info("test received from app is" + successText)

        assert "Success! Thank you!" in successText
        self.driver.get_screenshot_as_file("screen.png")