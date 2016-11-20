import unittest

from amity_lib.models import Staff, Person


class TestStaffClass(unittest.TestCase):

    def setUp(self):
        self.staff = Staff("John Maina")

    def test_is_subclass_person(self):
        self.assertIsInstance(self.staff, Person,
                              msg="The class Staff should extend Person class")

    def test_create_new_staff_instance(self):
        self.assertRaises(ValueError, Staff, "",
                          msg="Cannot create staff with empty name")
        self.assertEqual("John Maina", self.staff.get_name(),
                         msg="Staff name should be John Maina")
