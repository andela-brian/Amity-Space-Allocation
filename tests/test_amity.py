import unittest

import mock

from amity_lib.amity import Amity
from amity_lib.models import Office, LivingSpace


class TestAmity(unittest.TestCase):
    def setUp(self):
        self.amity = Amity()

    @mock.patch.dict('amity_lib.amity.Amity.offices', {'available': {'Hogwarts': Office('Hogwarts')}})
    def test_create_office(self):
        self.assertEqual('Created Office Summer', self.amity.create_office("Summer"),
                         msg='Should create a new Office named Summer')
        offices = self.amity.get_rooms()['offices']['available'].keys()
        self.assertItemsEqual(['Hogwarts', 'Summer'], offices,
                              msg='Available Offices should be Summer and Hogwarts')
        self.assertRaises(ValueError, self.amity.create_office("Hogwarts"),
                          msg='Cannot create duplicate Office Hogwarts')
        self.assertRaises(ValueError, self.amity.create_office(""),
                          msg='Cannot create Office with empty Name')
        self.assertRaises(ValueError, self.amity.create_office(123),
                          msg='Cannot create Office with only digits as name')

    @mock.patch.dict('amity_lib.amity.Amity.living_spaces', {'available': {'Shell': LivingSpace('Shell')}})
    def test_create_living_space(self):
        self.assertEqual('Created Living Space Perl', self.amity.create_living_spaces("Perl"),
                         msg='Should create a new Living Space Shell')
        living_spaces = self.amity.get_rooms()['living_spaces']['available'].keys()
        self.assertItemsEqual(['Shell', 'Perl'], living_spaces,
                              msg="Available Living spaces should be Perl and Shell")
        self.assertRaises(ValueError, self.amity.create_living_spaces("Shell"),
                          msg="Cannot create duplicate living space Shell")
        self.assertRaises(ValueError, self.amity.create_living_spaces(""),
                          msg="cannot create Living Space with empty name")
        self.assertRaises(ValueError, self.amity.create_living_spaces(123),
                          msg="Cannot create Living Space with only digits as name")

    @mock.patch.dict('amity_lib.amity.Amity.living_spaces', {'available': {'Shell': LivingSpace('Shell')}})
    @mock.patch.dict('amity_lib.amity.Amity.offices', {'available': {'Hogwarts': Office('Hogwarts')}})
    def test_create_fellow(self):
        self.assertDictEqual({'id': 'FL001', 'name': 'Kimani John', 'office': 'Hogwarts', 'living_space': None},
                             self.amity.create_fellow('Kimani John'),
                             msg="should create Fellow Kimani John with ID FL001 assigned Hogwarts Office Space")
        self.assertDictEqual({'id': 'FL002', 'name': 'Joshua Simeon', 'office': 'Hogwarts', 'living_space': 'Shell'},
                             self.amity.create_fellow('Joshua Simeon', accommodation='Y'),
                             msg="should create Fellow Joshua Simeon with ID FL002 assigned Hogwarts Office Space and Shell Living Space")
        self.assertRaises(ValueError, self.amity.create_fellow(""),
                          msg="Fellow name should not be empty")
        self.assertRaises(TypeError, self.amity.create_fellow(123),
                          msg="Fellow name should contain only Alphabetical Characters")
        self.assertRaises(ValueError, self.amity.create_fellow("Johhny Bravo", accommodation='X'),
                          msg="Excepted values for accommodation is Y and N")

    @mock.patch.dict('amity_lib.amity.Amity.offices', {'available': {'Hogwarts': Office('Hogwarts')}})
    def test_create_staff(self):
        self.assertDictEqual({'id': 'FL001', 'name': 'Kimani John', 'office': 'Hogwarts'},
                             self.amity.create_staff('Kimani John'),
                             msg="should create Staff Kimani John with ID ST001 assigned Hogwarts Office Space")
        self.assertRaises(ValueError, self.amity.create_staff(""),
                          msg="Staff name cannot be empty")
        self.assertRaises(TypeError, self.amity.create_staff(123),
                          msg="Staff name should be alphabetical characters")

    @mock.patch.dict('amity_lib.amity.Amity.offices', {'available': {'Hogwarts': Office('Hogwarts'), 'Blue': Office('Blue')}})
    @mock.patch.dict('amity_lib.amity.Amity.living_spaces', {'available': {'Shell': LivingSpace('Shell'), 'Perl': LivingSpace('Perl')}})
    def test_relocate_person(self):
        staff_id = 'ST001'
        fellow_id = 'FL001'
        pass
