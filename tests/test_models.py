import unittest

import mock

from amity_lib.models import Staff, Fellow, Office


class TestStaffClass(unittest.TestCase):

    def setUp(self):
        self.staff = Staff("John Maina")

    def test_create_new_staff_instance(self):
        self.assertEqual("John Maina", self.staff.get_name(),
                         msg="Staff name should be John Maina")


class TestFellowClass(unittest.TestCase):
    def setUp(self):
        self.fellow = Fellow("Brian Mali")

    def test_create_new_staff_instance(self):
        self.assertEqual("Brian Mali", self.fellow.get_name(),
                         msg="Staff name should be Brian Mali")


class TestOfficeClass(unittest.TestCase):
    def setUp(self):
        self.office = Office("Lilac")

    def test_office_capacity(self):
        self.assertEqual(6, self.office.get_capacity(),
                         msg="Office capacity should be 6")

    @mock.patch('amity_lib.models.Office.persons_id', ['FL001', 'ST001', 'FL003'])
    def test_allocate_space(self):
        self.assertTrue(self.office.is_available(), msg="Office should be available when not full")
        self.assertEqual('ST002 allocated Lilac', self.office.allocate_space('ST002'),
                         msg="ST002 should be allocated space in Lilac")
        self.assertRaises(ValueError, self.office.allocate_space('FL003'),
                          msg="cannot allocate person to a full room")
