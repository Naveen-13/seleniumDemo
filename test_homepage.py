import pytest
from selenium.webdriver.support.select import Select

from PageObjects.homePage import homePage
from TestData.HomePageData import homePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_homepage(self, getData):
        log = self.getLogger()
        homepage = homePage(self.driver)
        log.info("Name is " + getData["Name"])
        homepage.enterName().send_keys(getData["Name"])
        log.info("Email is " + getData["Email"])
        homepage.enterEmail().send_keys(getData["Email"])
        homepage.enterPassword().send_keys(getData["Password"])
        self.selectOptionByText(homepage.selectGender(), getData["Gender"])
        homepage.selectEmployment().click()
        homepage.selectSubmit().click()

    @pytest.fixture(params=homePageData.test_homeData)
    def getData(self, request):
        return request.param

