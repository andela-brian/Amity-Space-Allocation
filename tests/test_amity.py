import unittest

import mock

from amity_lib.amity import Amity


class TestAmity(unittest.TestCase):
    def setUp(self):
        self.amity = Amity()

    @mock.patch.dict('amity_lib.amity.Amity.offices',
                     {'available': {'Hogwarts'},
                      'unavailable': {}
                      })
    def test_create_office(self):
        pass
