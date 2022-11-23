import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]

        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler("logfile.log")

        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s ")

        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        logger.setLevel(logging.INFO)

        return logger

    # def take_screenshot(self,test_name):
    #     screenshots_dir = "C:\\Users\\Prith\\PycharmProjects\\TravelBooking\\Tests\\Test_screenshot"
    #     screenshot_file_path = "{}/{}.png".format(screenshots_dir,test_name)
    #     self.save_screenshot(screenshot_file_path)



