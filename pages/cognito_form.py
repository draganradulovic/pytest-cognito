import time
from base.selenium_driver import Selenium_actions
from selenium.webdriver.common.by import By


#Cognito_form child-class contains locators for every element on cognito form and methods used to manipulate form.
class Cognito_form(Selenium_actions):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

        #LOCATORS (xpath to each element. XPATHS are based mostly on ID-s and classes.
    _first_name_field="//*[@id='cog-0']"
    _last_name_field="//*[@id='cog-1']"
    _ssn_field="//*[@id='cog-2']"
    _address_1_field="//*[@id='cog-3-line1']"
    _address_2_field="//*[@id='cog-3-line2']"
    _region_field="//*[@id='cog-3-international-state']"
    _zip_code_field="//*[@id='cog-3-postal-code']"
    _country_field="//*[@id='cog-3-country']"
    _date_of_birth_field="//*[@id='cog-4']"
    _date_of_death_field="//*[@id='cog-5']"
    _email_field="//*[@id='cog-11']"
    _work_phone_field="//*[@id='cog-12']"
    _preferred_contact_field="//*[@id='cog-13']"
    _single_checkbox="//*[@class='el-checkbox-group']//label[1]//span[1]//span[1]"
    _married_checkbox="//*[@class='el-checkbox-group']//label[2]//span[1]//span[1]"
    _widowed_checkbox="//*[@class='el-checkbox-group']//label[3]//span[1]//span[1]"
    _divorced_checkbox="//*[@class='el-checkbox-group']//label[4]//span[1]//span[1]"
    _active_smoker_radio="//*[@class='el-radio-group']//label[1]//span[1]//span[1]"
    _good_exercise_routine_radio="//*[@class='el-radio-group']//label[2]//span[1]//span[1]"
    _alcohol_consumption_radio="//*[@class='el-radio-group']//label[3]//span[1]//span[1]"
    _healthy_sleep_habits_radio="//*[@class='el-radio-group']//label[4]//span[1]//span[1]"
    _username_field="//*[@id='cog-8']"
    _upload_button="//button[@class='el-button cog-button--secondary cog-upload__upload-button el-button--default cog-button']"
    _upload_dropzone="//input[@class='el-upload__input']"
    _save_button="//button[@class='el-button cog-button--has-status cog-button--primary cog-button--navigation el-button--default cog-button cog-button--submit']"

        #ERROR MESSAGE LOCATRORS:
    _empty_first_name_error= "//div[contains(text(),'First Name is required.')]"
    _invalid_first_name_error= "//div[contains(text(),'First Name must only contain letters.')]"
    _empty_last_name_error= "//div[contains(text(),'Lastname is required')]"
    _invalid_last_name_error = "//div[contains(text(),'Lastname must only contain letters.')]"
    _invalid_zip_format_error= "//div[contains(text(),'Zip Code must be formatted as #####-####.')]"
    _empty_address_info_error= "//div[contains(text(),'Address Line 1, State and Postal / Zip Code are required.')]"
    _empty_email_error= "//div[contains(text(),'Email is required.')]"
    _invalid_email_format_error= "//div[contains(text(),'Incorrect email format.')]"
    _empty_username_error = "//div[contains(text(),'Username is required.')]"
    _invalid_work_phone_format_error= "//div[contains(text(),'Work Phone must be formatted as ###-###-#### x####.')]"
    _invalid_birth_date_format_error= "//div[contains(text(),'Date Of Birth is not properly formatted.')]"
    _invalid_birth_date_range_error= "//div[contains(text(),'Date Of Birth must be between 1/1/1900 and today's date.')]"
    _invalid_death_date_format_error= "//div[contains(text(),'Date Of death is not properly formatted.')]"
    _invalid_death_date_range_error= "//div[contains(text(),'Date Of death must be between 1/1/2010 and today's date.')]"
    _invalid_ssn_field_format_error= "//div[contains(text(),'SSN field must contain 9 letters or remain empty.')]"
    _invalid_photo_format_error= "//div[contains(text(),'Format not supported.')]"

    def enter_first_name(self,key):
        self.send_keys(key, self._first_name_field)

    def enter_last_name(self,key):
        self.send_keys(key, self._last_name_field)

    def enter_ssn(self,key):
        self.send_keys(key,self._ssn_field)

    def enter_address_1(self, key):
        self.send_keys(key, self._address_1_field)

    def enter_address_2(self, key):
        self.send_keys(key, self._address_2_field)

    def enter_region(self, key):
        self.send_keys(key,self._region_field)

    def enter_zip_code(self, key):
        self.send_keys(key,self._zip_code_field)

    def enter_country(self, key):
        self.send_keys(key,self._country_field)

    # method selects country form list box.
    def select_country(self, key):
        self.scroll_by_elem(self._country_field)
        self.click_element(self._country_field)

        # UlElement variable contains whole unordered list element.
        ulElement=self.get_element("//*[@id='cog-3-country-listbox']")

        # Text inside every <li> tag is stored inside liElements variable, as list.
        liElements=ulElement.find_elements(By.TAG_NAME, 'li')

        #Looping through liElements. When liElements element is equal to given key, that element is being selected(clicked).
        for element in liElements:
            if key in element.text:
                self.click_element(self._country_field)
                element.click()
                break

    def enter_birth_date(self, key):
        self.send_keys(key, self._date_of_birth_field)

    #Method selects date from calendar.
    def select_birth_date(self, date1):
        #Date is given in format m/d/yy, so it has to be splitted to month, day and year
        date1=date1.split("/")
        month=date1[0]
        months={'1':'January', '2':'February', '3':'March', '4':'April', '5':'May', '6':'June', '7':'July', '8':'August',
                '9':'September', '10':'October', '11':'November', '12':'December'}
        day=date1[1]
        year=date1[2]
        self.scroll_by_elem(self._date_of_birth_field)
        self.click_element(self._date_of_birth_field)
        #year_down is the button on calendar used for navigating to previous year.
        year_down = self.get_element("//button[@aria-label='Previous Year']")
        #month_down is the button on calendar used for navigating to previous month.
        month_down= self.get_element("//button[@aria-label='Previous Month']")
        #_curr_month is element which shows current selected month.
        _curr_month="//*[@class='el-date-picker__header-label'][position()=2]"
        _curr_year="//*[@class='el-date-picker__header-label'][position()=1]"

        #clicking on date of birth field to be sure calendar is opened
        self.click_element(self._date_of_birth_field)
        #This loop chooses previous months until wanted month is selected.
        while self.get_element(_curr_month).text != months[month]:
            month_down.click()
        while self.get_element(_curr_year).text != year:
            year_down.click()
        time.sleep(2)
        #At the end, day is selected by clicking on correct number in calendar.
        date11 = self.get_element("(/html//table[1]//td[not(@class='is-muted')]//span[normalize-space()='"+day+"'])")
        date11.click()

    def enter_death_date(self, key):
        self.send_keys(key, self._date_of_death_field)

    def select_death_date(self, date1):
        date1 = date1.split("/")
        month = date1[0]
        months = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July',
                  '8': 'August','9': 'September', '10': 'October', '11': 'November', '12': 'December'}
        day = date1[1]
        year = date1[2]
        self.scroll_by_elem(self._date_of_death_field)
        self.click_element(self._date_of_death_field)
        year_down = self.get_element("(//button[@aria-label='Previous Year'])[2]")
        month_down = self.get_element("(//button[@aria-label='Previous Month'])[2]")
        _curr_month = "(//*[@class='el-date-picker__header-label'][position()=2])[2]"
        _curr_year = "(//*[@class='el-date-picker__header-label'][position()=1])[2]"

        self.click_element(self._date_of_death_field)
        while self.get_element(_curr_month).text != months[month]:
            month_down.click()
        while self.get_element(_curr_year).text != year:
            year_down.click()
        time.sleep(2)
        sel_date = self.get_element("(/html//table[1]//td[not(@class='is-muted')]//span[normalize-space()='"+day+"'])[2]")
        sel_date.click()

    def enter_email(self, key):
        self.send_keys(key, self._email_field)

    def enter_work_phone(self, key):
        self.send_keys(key, self._work_phone_field)

    def enter_preferred_contact(self, key):
        self.click_element(self._preferred_contact_field)
        self.send_keys(key, self._preferred_contact_field)

    #method selects preferred contact form list box.
    def select_preferred_contact(self, key):
        self.scroll_by_elem(self._preferred_contact_field)
        self.click_element(self._preferred_contact_field)

        #UlElement variable contains whole unordered list element.
        ulElement = self.get_element("//*[@id='cog-13-listbox']")

        #Text inside every <li> tag is stored inside liElements variable, as list.
        liElements = ulElement.find_elements(By.TAG_NAME, 'li')

        #Looping through liElements. When liElements element is equal to given key, that element is being selected(clicked).
        for element in liElements:
            if key in element.text:
                self.click_element(self._preferred_contact_field)
                element.click()
                break

    #selecting checkbox in marital status section
    def maritial_status_checkbox(self, item):
        item=item.lower()
        items={'single':self._single_checkbox, 'married':self._married_checkbox, 'widowed':self._widowed_checkbox,'divorced':self._divorced_checkbox}
        for i in items:
            if i == item:
                self.scroll_by_elem(items[i])
                self.click_element(items[i])

    #selecting radio button in health behaviors radio input section.
    def health_behaviors_radio(self, item):
        item = item.lower()
        items = {'active smoker': self._active_smoker_radio, 'good exercise routine': self._good_exercise_routine_radio,
                 'alcohol consumption': self._alcohol_consumption_radio, 'healthy sleep habits': self._healthy_sleep_habits_radio}
        for i in items:
            if i == item:
                self.scroll_by_elem(items[i])
                self.click_element(items[i])

    def upload_photo(self, photo_name):
        path=(r"C:\Users\User\PycharmProjects\CognitoForm\utilities\csv_data_files")
        self.get_element(self._upload_dropzone).send_keys(path+photo_name)

    def enter_username(self, key):
        self.send_keys(key, self._username_field)
        time.sleep(5)

    #Fills out mandatory fields of the cognito form.
    def create_new_using_mandatory_fields(self, first_name, last_name, address, region, zip, country, email, username):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_address_1(address)
        self.enter_region(region)
        self.enter_zip_code(zip)
        self.select_country(country)
        self.enter_email(email)
        self.enter_username(username)
        self.click_element(self._save_button)

    #Fills out all fields of the cognito form using send_keys method for all fields.
    def create_new_using_all_fields_input(self, first_name="", last_name="", ssn="", address1="", address2="", region="", zip="",
                                          country="", bitrh_date="", death_date="", email="", work_phone="", preffered_contact="",
                                          marital_status="", health_behaviors="",username="", photo_name=""):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_ssn(ssn)
        self.enter_address_1(address1)
        self.enter_address_2(address2)
        self.enter_region(region)
        self.enter_zip_code(zip)
        self.enter_country(country)
        self.enter_birth_date(bitrh_date)
        self.enter_death_date(death_date)
        self.enter_email(email)
        self.enter_work_phone(work_phone)
        self.enter_preferred_contact(preffered_contact)
        self.maritial_status_checkbox(marital_status)
        self.health_behaviors_radio(health_behaviors)
        if photo_name != "":
            self.upload_photo(photo_name)
        self.enter_username(username)
        self.click_element(self._save_button)

    #Fills out all fields of the cognito form by selecting items from list box when required and sending keys when necessary.
    def create_new_using_all_fields_select(self, first_name="", last_name="", ssn="", address1="", address2="", region="", zip="",
                                           country="", bitrh_date="", death_date="", email="", work_phone="", preffered_contact="",
                                           marital_status="", health_behaviors="",username="", photo_name=""):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_ssn(ssn)
        self.enter_address_1(address1)
        self.enter_address_2(address2)
        self.enter_region(region)
        self.enter_zip_code(zip)
        self.select_country(country)
        self.select_birth_date(bitrh_date)
        self.select_death_date(death_date)
        self.enter_email(email)
        self.enter_work_phone(work_phone)
        self.select_preferred_contact(preffered_contact)
        self.maritial_status_checkbox(marital_status)
        self.health_behaviors_radio(health_behaviors)
        if photo_name != "":
            self.upload_photo(photo_name)
        self.enter_username(username)
        self.click_element(self._save_button)

    #checks if user is created
    def is_user_created(self):
        try:
            self.get_element(self._save_button)
            return False
        except:
            return True

    #Method checks if given error is visible
    def is_error_visible(self,error):
        try:
            self.get_element(error)
            return True
        except:
            return False




