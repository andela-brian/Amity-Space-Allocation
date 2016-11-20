import unittest

import mock

from amity_lib.models import Staff, Fellow, Office, LivingSpace


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

    @mock.patch('amity_lib.models.Office.persons_id', ['FL001', 'ST001', 'FL003', 'ST004', 'ST002'])
    def test_allocate_space(self):
        self.assertTrue(self.office.is_available(), msg="Office should be available when not full")
        self.assertRaises(ValueError, self.office.allocate_space('S001'),
                          msg="The person_id prefix should be 'ST' or 'FL'")
        self.assertEqual('ST002 allocated Lilac', self.office.allocate_space('ST002'),
                         msg="ST002 should be allocated space in Lilac")
        self.assertRaises(ValueError, self.office.allocate_space('FL003'),
                          msg="cannot allocate person to a full room")


class TestLivingSpaceClass(unittest.TestCase):
    def setUp(self):
        self.living_space = LivingSpace("Shell")

    def test_get_capacity(self):
        self.assertEqual(4, self.living_space.get_capacity(),
                         msg="Living Space capacity should be 4")

    @mock.patch('amity_lib.models.LivingSpace.persons_id', ['FL001', 'FL002', 'FL003'])
    def test_allocate_space(self):
        self.assertTrue(self.living_space.is_available(), msg="Living Space should be available when not full")
        self.assertRaises(ValueError, self.living_space.allocate_space('S001'),
                          msg="The person_id prefix should be 'ST' or 'FL'")
        self.assertRaises(ValueError, self.living_space.allocate_space('ST001'),
                          msg="Cannot allocate Staff to Living Space")
        self.assertEqual('FL004 allocated Lilac', self.living_space.allocate_space('FL004'),
                         msg="FL004 should be allocated space in Shell")
        self.assertRaises(ValueError, self.living_space.allocate_space('FL005'),
                          msg="Cannot allocate fellow to a full Living Space")
