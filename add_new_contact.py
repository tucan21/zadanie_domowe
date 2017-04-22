# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class add_new_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_new_contact(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", passwort="secret")
        self.init_contact_form(wd)
        self.fill_new_contact_form(wd, Contact(firstname="Jan", middlename="Paweł", address="Kraków", mobile="625365965", email="test@onet.pl"))
        self.logout(wd)
        self.assertTrue(success)

    def test_add_new_2nd_contact(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", passwort="secret")
        self.init_contact_form(wd)
        self.fill_new_contact_form(wd, Contact(firstname="Ola", middlename="Kasia", address="Warszawa", mobile="785236589", email="ola@onet.pl"))
        self.logout(wd)
        self.assertTrue(success)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def fill_new_contact_form(self, wd, contact):
        # fill new contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # submit new contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def init_contact_form(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, passwort):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(passwort)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost:81/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
