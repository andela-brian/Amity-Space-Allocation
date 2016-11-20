import unittest

import mock

from amity_lib.amity import Amity
from amity_lib.models import Office


class TestAmity(unittest.TestCase):
    def setUp(self):
        self.amity = Amity()

    @mock.patch.dict('amity_lib.amity.Amity.offices',
                     {'available': {'Hogwarts': Office('Hogwarts')}
                      })
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
                          msg='Cannot create Office with numbers as name')
