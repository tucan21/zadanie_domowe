# -*- coding: utf-8 -*-
from aplikacja import Aplikacja
from model.contact import Contact
import pytest


@pytest.fixture
def app(request):
    fixture = Aplikacja
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.login(username="admin", passwort="secret")
    app.fill_new_contact_form(Contact(firstname="Jan", middlename="Paweł", address="Kraków", mobile="625365965", email="test@onet.pl"))
    app.logout()


def test_add_new_2nd_contact(app):
    app.login(username="admin", passwort="secret")
    app.fill_new_contact_form(Contact(firstname="Ola", middlename="Kasia", address="Warszawa", mobile="785236589", email="ola@onet.pl"))
    app.logout()
