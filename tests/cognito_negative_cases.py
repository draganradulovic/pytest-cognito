import unittest
import pytest
from pages.cognito_form import Cognito_form
from ddt import ddt,data,unpack
from utilities.csv_reader import get_csv_data
import os



@pytest.mark.usefixtures('oneTimeSetUp','setUp7')
@ddt
class Cognito_negative_cases(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self, oneTimeSetUp, setUp7):
        self.cf=Cognito_form(self.driver)


    @pytest.mark.run(order=1)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities','csv_data_files', 'test_invalid_first_name_data.csv'))))
    @unpack
    def test_invalid_first_name(self,first_name, last_name, address, region, zip, country, email, username):
        self.cf.create_new_using_mandatory_fields(first_name, last_name, address, region, zip, country, email, username)
        result = self.cf.is_error_visible(self.cf._invalid_first_name_error)
        assert result == True

    @pytest.mark.run(order=1)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities','csv_data_files', 'test_invalid_last_name_data.csv'))))
    @unpack
    def test_invalid_last_name(self, first_name, last_name, address, region, zip, country, email, username):
        self.cf.create_new_using_mandatory_fields(first_name, last_name, address, region, zip, country, email, username)
        result = self.cf.is_error_visible(self.cf._invalid_last_name_error)
        assert result == True

    @pytest.mark.run(order=1)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities','csv_data_files', 'test_invalid_ssn_data.csv'))))
    @unpack
    def test_invalid_ssn(self, first_name, last_name, ssn, address1, address2, region,zip,country,birth_date,death_date,
                         email,work_phone,preffered_contact,maritial_status,health_behaviors,username,photo_name):
        self.cf.create_new_using_all_fields_input(first_name, last_name, ssn, address1, address2, region,zip,country,birth_date,
                                                  death_date,email,work_phone,preffered_contact,maritial_status,health_behaviors,username,photo_name)
        result = self.cf.is_error_visible(self.cf._invalid_ssn_field_format_error)
        assert result == True

    @pytest.mark.run(order=1)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities','csv_data_files', 'test_invalid_zip.csv'))))
    @unpack
    def test_invalid_zip(self, first_name, last_name, address, region, zip, country, email, username):
        self.cf.create_new_using_mandatory_fields(first_name, last_name, address, region, zip, country, email, username)
        result = self.cf.is_error_visible(self.cf._invalid_zip_format_error)
        assert result == True

    @pytest.mark.run(order=1)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities','csv_data_files', 'test_invalid_date_of_birth_format_data.csv'))))
    @unpack
    def test_invalid_date_of_birth_format(self, first_name, last_name, ssn, address1, address2, region, zip, country, birth_date,
                                          death_date, email, work_phone, preffered_contact, maritial_status, health_behaviors, username,photo_name):
        self.cf.create_new_using_all_fields_input(first_name, last_name, ssn, address1, address2, region, zip, country,birth_date,
                                                  death_date, email, work_phone, preffered_contact,maritial_status, health_behaviors, username, photo_name)
        result = self.cf.is_error_visible(self.cf._invalid_birth_date_format_error)
        assert result == True

    @pytest.mark.run(order=1)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities','csv_data_files', 'test_invalid_date_of_birth_range_data.csv'))))
    @unpack
    def test_invalid_date_of_birth_range(self, first_name, last_name, ssn, address1, address2, region, zip, country,birth_date,
                                         death_date, email, work_phone, preffered_contact, maritial_status,health_behaviors, username, photo_name):
        self.cf.create_new_using_all_fields_input(first_name, last_name, ssn, address1, address2, region, zip, country,birth_date,
                                                  death_date, email, work_phone, preffered_contact,maritial_status, health_behaviors, username, photo_name)
        result = self.cf.is_error_visible(self.cf._invalid_birth_date_range_error)
        assert result == True

    @pytest.mark.run(order=1)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities','csv_data_files', 'test_invalid_date_of_death_format_data.csv'))))
    @unpack
    def test_invalid_date_of_death_format(self, first_name, last_name, ssn, address1, address2, region, zip, country,birth_date,
                                          death_date, email, work_phone, preffered_contact, maritial_status,health_behaviors, username, photo_name):
        self.cf.create_new_using_all_fields_input(first_name, last_name, ssn, address1, address2, region, zip, country,birth_date,
                                                  death_date, email, work_phone, preffered_contact,maritial_status, health_behaviors, username, photo_name)
        result = self.cf.is_error_visible(self.cf._invalid_death_date_format_error)
        assert result == True

    @pytest.mark.run(order=1)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities','csv_data_files', 'test_invalid_date_of_death_range_data.csv'))))
    @unpack
    def test_invalid_date_of_death_range(self, first_name, last_name, ssn, address1, address2, region, zip, country,birth_date,
                                         death_date, email, work_phone, preffered_contact, maritial_status,health_behaviors, username, photo_name):
        self.cf.create_new_using_all_fields_input(first_name, last_name, ssn, address1, address2, region, zip, country,birth_date,
                                                  death_date, email, work_phone, preffered_contact,maritial_status, health_behaviors, username, photo_name)
        result = self.cf.is_error_visible(self.cf._invalid_death_date_range_error)
        assert result == True

    @pytest.mark.run(order=1)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities','csv_data_files', 'test_invalid_email_data.csv'))))
    @unpack
    def test_invalid_email(self, first_name, last_name, address, region, zip, country, email, username):
        self.cf.create_new_using_mandatory_fields(first_name, last_name, address, region, zip, country, email, username)
        result = self.cf.is_error_visible(self.cf._invalid_email_format_error)
        assert result == True

    @pytest.mark.run(order=1)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities','csv_data_files', 'test_invalid_photo_format_data.csv'))))
    @unpack
    def test_invalid_photo_format(self, first_name, last_name, ssn, address1, address2, region, zip, country,birth_date,
                                  death_date, email, work_phone, preffered_contact, maritial_status,health_behaviors, username, photo_name):
        self.cf.create_new_using_all_fields_input(first_name, last_name, ssn, address1, address2, region, zip, country,birth_date,
                                                  death_date, email, work_phone, preffered_contact,maritial_status, health_behaviors, username, photo_name)
        result = self.cf.is_error_visible(self.cf._invalid_photo_format_error)
        assert result == True

    #Will be added
    #def test_ivalid_work_phone_format(self):

    #Will be added
    #def test_invalid_work_phone_range(self):

    @pytest.mark.run(order=1)
    @data(*get_csv_data(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'utilities','csv_data_files', 'test_all_empty_fields_data.csv'))))
    @unpack
    def test_all_empty_fields(self, first_name, last_name, address, region, zip, country, email, username):
        self.cf.create_new_using_mandatory_fields(first_name, last_name, address, region, zip, country, email, username)
        assert self.cf.is_error_visible(self.cf._empty_first_name_error)
        assert self.cf.is_error_visible(self.cf._empty_last_name_error)
        assert self.cf.is_error_visible(self.cf._empty_address_info_error)
        assert self.cf.is_error_visible(self.cf._empty_email_error)
        assert self.cf.is_error_visible(self.cf._empty_username_error)

