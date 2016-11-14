from unittest import TestCase
from mock import patch


class TestAmityClass(TestCase):
    def setUp(self):
        self.amity = Amity()

    def test_default_values(self):
        self.assertListEqual(
            [0, 0],
            [
                len(self.amity.get_unallocated_staff()),
                len(self.amity.get_unallocated_fellows())
            ],
            msg="The unallocated fellows and staff should be 0 on creation of Amity Object")

        self.assertListEqual(
            [0, 0],
            [
                len(self.amity.get_rooms()['offices']['available']),
                len(self.amity.get_rooms()['offices']['unavailable'])
            ],
            msg="The available and unavailable offices should be empty on creating new amity object"
        )

        self.assertListEqual(
            [0, 0],
            [
                len(self.amity.get_rooms()['living_spaces']['available']),
                len(self.amity.get_rooms()['living_spaces']['unavailable'])
            ],
            msg="The available and unavailable living rooms should be empty on creating new amity object"
        )

    def test_create_fellow(self):
        self.amity = Amity()
        self.amity.create_living_space("Perl")
        self.amity.create_office("Homer")
        self.amity.create_fellow(first_name="John", other_name="Dow", accomodation='Y')
        self.amity.create_fellow(first_name="Brian", other_name="Kimani")

    @patch.dict('Amity.rooms', {'offices': ['Summer', 'Winter'], 'living_spaces': ['Shell', 'Perl']})
    def test_create_rooms(self):
        offices = self.amity.get_rooms()['offices']
        living_spaces = self.amity.get_rooms()['living_spaces']

        self.assertListEqual(["Summer", "Winter"], offices,
                             msg="Offices in Amity should be Summer and Winter")

        self.assertListEqual(["Lime", "Blue"],
                             living_spaces,
                             msg="Living Spaces in Amity should be Lime and Blue")
