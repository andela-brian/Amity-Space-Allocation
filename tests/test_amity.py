from unittest import TestCase

import mock


class TestAmityClass(TestCase):
    def setUp(self):
        self.amity = Amity()

    @mock.patch.dict('amity_lib.amity.Amity.offices', {'available': [OfficeSpace('Summer')], 'unavailable': []})
    @mock.patch.dict('amity_lib.amity.Amity.living_spaces', {'available': [LivingSpace('Shell')], 'unavailable': []})
    def test_create_fellow(self):
        self.amity.create_fellow(first_name="John", other_name="Dow", accomodation='Y')
        self.amity.create_fellow(first_name="Brian", other_name="Kimani")

        self.assertEqual(2,
                         len(self.amity.get_rooms()['offices']['available'][0].get_allocations()),
                         msg="Two fellows should be assigned to the Summer Office Space")
        self.assertEqual(1,
                         len(self.amity.get_rooms()['living_spaces']['available'][0].get_allocations()),
                         msg="One Fellow should be assigned a Living Space at Shell")

    @mock.patch.dict('amity_lib.amity.Amity.offices', {'available': [OfficeSpace('Summer'), OfficeSpace('Winter')]})
    @mock.patch.dict('amity_lib.amity.Amity.living_spaces', {'available': [LivingSpace('Shell'), LivingSpace('Perl')]})
    def test_create_rooms(self):
        self.assertItemsEqual(["Summer", "Winter"],
                              [office.get_name() for office in self.amity.get_rooms()['offices']['available']],
                              msg="Offices in Amity should be Summer and Winter")
        self.assertItemsEqual(["Shell", "Perl"],
                              [living_space.get_name() for living_space in
                               self.amity.get_rooms()['living_spaces']['available']],
                              msg="Living Spaces in Amity should be Shell and Perl")

        self.assertEqual('Room Summer Exists', self.amity.create_office("Summer"),
                         msg='an error should be returned if a room with the same name exists')
        self.assertEqual('Created Room Lilac', self.amity.create_office("Lilac"),
                         msg='A new room named Lilac should be created')
