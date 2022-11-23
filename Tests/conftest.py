import os.path

import openpyxl
import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.service import Service
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from urllib3.util import request

from Utilities.BaseClass import BaseClass


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="edge")
    parser.addoption("--url", action="store", default="edge")



@pytest.fixture(scope="class")
def setup(request, chrome_options=None):
    global driver
    browserName = request.config.getoption("browser_name")

    if browserName == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-error")
        chrome_options.add_argument("--ignore-ssl-errors")
        capabilities = chrome_options.to_capabilities()
        capabilities['acceptInsecureCerts'] = True

        services_obj = Service(r'C:\Users\Prith\Downloads\Testing\sel\chromedriver.exe')
        driver = webdriver.Chrome(service=services_obj, options=chrome_options)

    elif browserName == 'edge':
        services_obj = Service(r"C:\Users\Prith\Downloads\Testing\sel\msedgedriver.exe")
        driver = webdriver.Edge(service=services_obj)

        failed_before = request.session.testsfailed

    # driver.get("https://www.tripadvisor.in/")
    book = openpyxl.load_workbook(r"C:\\Users\\Prith\\Desktop\\Book2.xlsx")
    sheet2 = book['Sheet2']
    URl = sheet2.cell(2, 5).value
    driver.get(URl)
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()


# Take screenshot automatic when my test case fail (std code)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("http://www.rcvacadmy.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = report.nodeid.replace("::", "_") + ".png"
            destinetionFile = os.path.join(report_directory, file_name)
            driver.save_screenshot(destinetionFile)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width=300px;height=200px"' \
                       'onclick="windo.open(this.src)" align="right"/></div>' % file_name
            extra.append(pytest_html.extras.html(html))
        report.extra = extra


# Report Name Std code
def pytest_html_report_title(report):
    report.title = "Tripadvisor HTML report!"
