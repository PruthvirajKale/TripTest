import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import pytest
from PageObject.HomePage import HomePage
from Utilities.BaseClass import BaseClass
from selenium.webdriver.support.ui import WebDriverWait
from TestData import Data
from TestData.Data import PageData


class TestBooking(BaseClass):
    @pytest.fixture(params=PageData.getTestData("CityName2"))
    def getData(self, request):
        return request.param

    def test_HolidayHomes(self, getData):
        log = self.getLogger()
        self.driver.implicitly_wait(30)

        homepage = HomePage(self.driver)

        Titleofpage = homepage.Title()
        assert "Tripadvisor" in Titleofpage

        log.info("Clicking on Holiday Homes")
        homepage.HolidayHomes().click()

        log.info("Entering City Names")
        homepage.Enter_City().send_keys(getData["City"])
        # homepage.Enter_City().send_keys("Mumbai")

        # self.verifyLinkPresence("Mumbai")
        log.info("Collecting list of cities and selecting Options ")
        list = homepage.CityList()

        for city in list:
            if city.text == "Mumbai, India":
                city.click()
                break

            else:
                city.is_selected()
                city.click()
                break

        log.info("Clicking on Calender and From Date")
        # if homepage.From_Date().is_displayed():
        #     assert True
        # else:
        #     # self.driver.get_screenshot_as_file("Test.png")
        #     self.driver.get_screenshot_as_file(r"C:\Users\Prith\PycharmProjects\TravelBooking\Tests.png")
        #     assert False

        homepage.From_Date().click()
        homepage.Date1().click()

        log.info("Clicking on Calender and To Date")
        homepage.To_date().click()
        homepage.Date2().click()

        log.info("Adding Guest")
        homepage.Add_Guest_Count().click()
        homepage.Guest_Addition().click()
        homepage.Guest_Addition().click()

        log.info("Applying Guest count")
        homepage.click_Apply().click()
        assert '4+' in homepage.GuestNumVerify()

        log.info("Displaying Filter")
        homepage.ShowAllFilter().click()

        # filter_list=homepage.FilterList()

        # // span[contains(text(), 'Elevator/Lift access')]
        # for filter in filter_list:
        #     if filter.text == "Elevator/Lift access(5)":
        #         filter.click()
        #         break
        log.info("Selecting Filter")

        homepage.Filter_element().click()
        # assert not homepage.Lift_Select().is_selected()

        log.info("Closing filter window")
        homepage.Closefilter().click()

        log.info("Sorting ")
        homepage.Sort_Rating().click()

        log.info("Clicking on Calender and From Date")
        homepage.SelectTravellerRating().click()

        assert "Traveller Rating" in homepage.TravelerRatingCheck().text

        log.info("Printing  the Hotel Names & Per Night charges")

        print("First Hotel Name is " + homepage.H_Home1())
        print("First Hotel Charges are " + homepage.H_Home1Charges())

        # wait = WebDriverWait.until(expected_conditions.presence_of_element_located((homepage.H_Home2())))
        print("Second Hotel Name is " + homepage.H_Home2())
        print("Second Hotel Charges are " + homepage.H_Home2Charges())
        #
        print("Third Hotel Name is " + homepage.H_Home3())
        print("Third Hotel Charges are " + homepage.H_Home3Charges())

        Msg = "Third Hotel Charges are " + homepage.H_Home3Charges()

        assert "per night" in homepage.H_Home3Charges()
