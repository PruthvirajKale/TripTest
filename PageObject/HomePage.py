import logging

from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver


    def Title(self):
        return self.driver.title
    Holiday_Homes = (By.XPATH, "(//span[@class='biGQs _P ttuOS'])[7]")

    def HolidayHomes(self):
        return self.driver.find_element(*HomePage.Holiday_Homes)

    Enter_city = (By.XPATH, "(//input[@title='Search'])[3]")

    def Enter_City(self):
        return self.driver.find_element(*HomePage.Enter_city)

    City_List = (By.XPATH, "(//a[@role='option'])/div[2]/div[1]")

    def CityList(self):
        return self.driver.find_elements(*HomePage.City_List)

    from_Date_1 = (By.ID, "CHECKIN_PICKER")
    # from_Date_1 = (By.XPATH, "(//span[@class='biGQs _P fiohW uWleQ'])[1]")

    def From_Date(self):
        return self.driver.find_element(*HomePage.from_Date_1)

    Date_1 = (By.XPATH, "//div[contains(@aria-label,'Fri Dec 16 2022')]")
    # Date_1 = (By.XPATH, "//div[contains(@aria-label,'16 December 2022')]")


    def Date1(self):
        return self.driver.find_element(*HomePage.Date_1)

    to_Date_1 = (By.ID, "CHECKOUT_PICKER")

    def To_date(self):
        return self.driver.find_element(*HomePage.to_Date_1)

    Date_2 = (By.XPATH, "//div[contains(@aria-label,'Tue Dec 20 2022')]")
    # Date_2 = (By.XPATH, "//div[contains(@aria-label,'20 December 2022')]")

    def Date2(self):
        return self.driver.find_element(*HomePage.Date_2)

    Add_Guest = (By.XPATH, "//div[@class='ujHpU f z u']")
    # Add_Guest = (By.XPATH, "//div[@class='yzRfM f']")

    def Add_Guest_Count(self):
        return self.driver.find_element(*HomePage.Add_Guest)

    Guest_numberAdd = (By.XPATH, "(//span[@class='ui_icon plus fBgDg S4'])[2]")
    # Guest_numberAdd = (By.XPATH, "(//button[@class='MnqWg S5 _S _H _W u j'])[4]")

    def Guest_Addition(self):
        return self.driver.find_element(*HomePage.Guest_numberAdd)

    GuestNum=(By.XPATH,"//div[@class='CztlA f b H4']")
    # GuestNum = (By.XPATH, "(//div[@class='PsGIp c'])[2]")

    def GuestNumVerify(self):
        return self.driver.find_element(*HomePage.GuestNum).text

    Apply = (By.XPATH, "(//div[@class='QjnOI P4'])//button")
    # Apply = (By.XPATH, "//button[@class='rmyCe _G B- z _S c Wc wSSLS jWkoZ sOtnj']")

    def click_Apply(self):
        return self.driver.find_element(*HomePage.Apply)

    Filter_showall = (By.XPATH, "//span[contains(text(),'Show all')][1]")
    # Filter_showall = (By.XPATH, "(//button[@class='UikNM _G B- _S _T c G_ P0 wSSLS TXrCr'])[1]")


    def ShowAllFilter(self):
        return self.driver.find_element(*HomePage.Filter_showall)

    Filter_list = (By.XPATH, "//span[@class='biGQs _P pZUbB KxBGd']")

    lift=(By.XPATH,"(//input[@type='checkbox'])[24]")

    def Lift_Select(self):
        return self.driver.find_element(*HomePage.lift)

    def FilterList(self):
        return self.driver.find_elements(*HomePage.Filter_list)

    Lift = (By.XPATH, "//span[contains(text(),'Elevator/Lift access')]")

    def Filter_element(self):
        return self.driver.find_element(*HomePage.Lift)

    CloseFilter = (By.XPATH, "//button[@aria-label='Close']")

    def Closefilter(self):
        return self.driver.find_element(*HomePage.CloseFilter)

    Filter_checkbox=(By.XPATH,"//span[@class='PMWyE _W I j u R2 _S ynMKU']")

    def Filter_cbox(self):
        return self.driver.find_element(*HomePage.Filter_checkbox)

    SortDD = (By.XPATH, "//span[contains(text(),'Tripadvisor Sort')]")

    def Sort_Rating(self):
        return self.driver.find_element(*HomePage.SortDD)

    Rating = (By.XPATH, "//span[contains(text(),'Traveller Rating')]")

    def SelectTravellerRating(self):
        return self.driver.find_element(*HomePage.Rating)

    Trating=(By.XPATH,"//div[@class='jvgKF B1 Z S4']")

    def TravelerRatingCheck(self):
        return self.driver.find_element(*HomePage.Trating)

    Home1 = (By.XPATH, "//div[@class='hGles Fn']/div[4]/div/div/div[2]/h2/a")

    def H_Home1(self):
        return self.driver.find_element(*HomePage.Home1).text


    Home1_Charges = (By.XPATH, "((//div[@class='zxMUq f'])/div/div[2]/div[1]/div[1])[1]")

    def H_Home1Charges(self):
        return self.driver.find_element(*HomePage.Home1_Charges).text

        # logging.INFO("Fetching details of second Home ")

    Home2 = (By.XPATH, "//div[@class='hGles Fn']/div[5]/div/div/div[2]/h2/a")

    # Home2 = (By.XPATH, "(//div[@class='zxMUq f'])/h2[2]")

    def H_Home2(self):
        return self.driver.find_element(*HomePage.Home2).text

    # Home2_Charges = (By.XPATH, "((//div[@class='zxMUq f'])/div/div[2]/div[1]/div[2])[2]")
    Home2_Charges = (By.XPATH, "((//div[@class='zxMUq f'])/div/div[2]/div[1]/div[1])[2]")

    def H_Home2Charges(self):
        return self.driver.find_element(*HomePage.Home2_Charges).text

        # logging.INFO("Fetching details of second Home ")

    Home3 = (By.XPATH, "//div[@class='hGles Fn']/div[6]/div/div/div[2]/h2/a")

    def H_Home3(self):
        return self.driver.find_element(*HomePage.Home3).text

    # Home3_Charges = (By.XPATH, "((//div[@class='zxMUq f'])/div/div[2]/div[1]/div[2])[3]")
    Home3_Charges = (By.XPATH, "((//div[@class='zxMUq f'])/div/div[2]/div[1]/div[1])[3]")

    def H_Home3Charges(self):
        return self.driver.find_element(*HomePage.Home3_Charges).text
