"""[Author: Chanh Duong. Student number: 040-681-356]
    """

from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
import unittest
from csvapp.views import record_list, record_form, record_download, record_delete

"""[Unit testing the View function connects to Url properly]
    """


class PageTest(TestCase):

    print('Chanh Duong 040-681-356')
    # Test view connected the url correctly
    # Test form url

    def test_record_form_url(self):
        url = reverse('record_insert')
        self.assertEqual(resolve(url).func, record_form)
    # Test List url

    def test_record_list_url(self):
        url = reverse('record_list')
        self.assertEqual(resolve(url).func, record_list)
    # Test Delete url

    def test_record_download_url(self):
        url = reverse('record_download')
        self.assertEqual(resolve(url).func, record_download)
    # Test Update url

    def test_record_update_url(self):
        url = reverse('record_update', kwargs={'id': 1})
        self.assertEqual(resolve(url).func, record_form)
    # Test Delete url

    def test_record_delete_url(self):
        url = reverse('record_delete', kwargs={'id': 1})
        self.assertEqual(resolve(url).func, record_delete)
