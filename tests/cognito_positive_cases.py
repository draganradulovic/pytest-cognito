import unittest
import pytest
from pages.cognito_form import Cognito_form
from ddt import ddt,data,unpack
from utilities.csv_reader import get_csv_data
import os

@pytest.mark.usefixtures('oneTimeSetUp','setUp7')
@ddt
class Cognito_positive_cases(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, oneTimeSetUp, setUp7):
        self.cf=Cognito_form(self.driver)

    @pytest.mark.run(order=1)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities','csv_data_files', 'positive_mandatory_fields.csv'))))
    @unpack
    def test_mandatory_fields(self,first_name, last_name, address, region, zip, country, email, username):
        self.cf.create_new_using_mandatory_fields(first_name, last_name, address, region, zip, country, email, username)
        result=self.cf.is_user_created()
        assert result == True

    @pytest.mark.run(order=2)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities','csv_data_files', 'positive_all_fields.csv'))))
    @unpack
    def test_all_fields_by_input(self,first_name, last_name, ssn, address1, address2, region, zip, country, birth_date, death_date,
                        email, work_phone,preferred_contact, maritial_status, health_behaviors,username,photo_name):
        self.cf.create_new_using_all_fields_input(first_name, last_name, ssn, address1, address2, region, zip, country,
                                                  birth_date, death_date, email, work_phone,preferred_contact, maritial_status,health_behaviors,username,photo_name)
        result = self.cf.is_user_created()
        assert result == True

    @pytest.mark.run(order=3)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities', 'csv_data_files', 'positive_all_fields.csv'))))
    @unpack
    def test_all_fields_by_selecting(self, first_name, last_name, ssn, address1, address2, region, zip, country, birth_date,
                                     death_date, email, work_phone, preferred_contact, maritial_status, health_behaviors, username,photo_name):
        self.cf.create_new_using_all_fields_select(first_name, last_name, ssn, address1, address2, region, zip, country,
                                                   birth_date, death_date, email, work_phone, preferred_contact,maritial_status, health_behaviors, username, photo_name)
        result = self.cf.is_user_created()
        assert result == True

