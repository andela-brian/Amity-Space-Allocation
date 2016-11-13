from unittest import TestCase


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

        allocations = self.amity.get_allocations()
        self.assertEqual(1, len(allocations['living_spaces']['Perl'].get_allocations()),
                         msg="Only One fellow should be allocated to Perl Living Space")
        self.assertEqual(2, len(allocations['offices']['Homer'].get_allocations()),
                         msg="Only Two fellows should be allocated to Homer office space")

    def test_create_rooms(self):
        self.amity = Amity()
        self.amity.create_living_space("Summer")
        self.amity.create_living_space("Winter")
        self.amity.create_office("Lime")
        self.amity.create_office("Blue")

        offices = self.amity.get_rooms()['offices']
        living_spaces = self.amity.get_rooms()['living_spaces']

        self.assertListEqual(["Summer", "Winter"],
                             offices,
                             msg="Offices in Amity should be Summer and Winter")

        self.assertListEqual(["Lime", "Blue"],
                             offices,
                             msg="Living Spaces in Amity should be Lime and Blue")
